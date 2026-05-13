import sys
import os
import networkx as nx
import matplotlib
matplotlib.use('Agg') # Set backend before importing pyplot
import matplotlib.pyplot as plt
from antlr4 import InputStream, CommonTokenStream, ParserRuleContext, TerminalNode
from antlr4.tree.Tree import ParseTreeWalker, ParseTreeListener

# Ensure we can run as script from inside src or root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.antlr_gen.GGCodeLexer import GGCodeLexer
from src.antlr_gen.GGCodeParser import GGCodeParser

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under CCSA.
    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.
    '''
    if not nx.is_tree(G):
        return nx.spring_layout(G)

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children)!=0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap,
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def build_graph(tree, parser):
    G = nx.DiGraph()
    labels = {}
    node_colors = {}

    counter = [0]

    # Skip rules that are just structural wrappers (if they have 1 child)
    SKIP_RULES_SINGLE_CHILD = {
        'statement', 'simpleStatement', 'compoundStatement',
        'motionStatement', 'machineStatement', 'geometryStatement', 'definitionStatement',
        'moveTarget', 'coordinateTarget', 'expression', 'primaryExpression',
        'unaryExpression', 'multiplicativeExpression', 'additiveExpression', 'comparisonExpression',
        'numericValue', 'blockStatement', 'locationDefinition', 'axisSingle', 'centerClause',
        'lengthClause', 'widthClause', 'radiusClause'
    }

    NICE_NAMES = {
        'repeatStatement': 'Repeat Loop',
        'conditionalStatement': 'If-Condition',
        'moveStatement': 'Move Cmd',
        'defineStatement': 'Define Loc',
        'setStatement': 'Set Var',
        'statementList': 'Block',
        'repeatCount': 'Count',
        'condition': 'Cond',
        'statement': 'Stmt',
        'blockStatement': 'Block',
        'coordinatePair': 'Coord',
        'pointTarget': 'Point',
        'axisSingle': 'Axis',
        'numericValue': 'Num',
        'program': 'Program'
    }

    # Colors
    COLOR_KEYWORD = '#ff9999' # Soft Red
    COLOR_LITERAL = '#eeeeee' # Light Grey
    COLOR_CONTROL = '#ffeebb' # Gold/Yellow
    COLOR_CMD     = '#cceeff' # Light Blue
    COLOR_ROOT    = '#ddddff' # Lavender

    KEYWORDS = {'Repeat', 'If', 'Define', 'Set', 'Move', 'to', 'as', 'times', 'then', 'else', '{', '}', 'Stop', 'Pause'}

    def get_color(label, is_terminal):
        if is_terminal:
            if label in KEYWORDS:
                return COLOR_KEYWORD
            return COLOR_LITERAL

        if 'Loop' in label or 'Condition' in label:
            return COLOR_CONTROL
        if 'Cmd' in label or 'Set' in label or 'Define' in label:
            return COLOR_CMD
        return COLOR_ROOT

    def simplify_walk(node, parent_id=None):
        is_terminal = isinstance(node, TerminalNode)

        rule_name = ""
        if not is_terminal:
            rule_index = node.getRuleIndex()
            rule_name = parser.ruleNames[rule_index]

        # Skip pass-through rules
        if not is_terminal and rule_name in SKIP_RULES_SINGLE_CHILD and node.getChildCount() == 1:
            return simplify_walk(node.getChild(0), parent_id)

        # Create Node
        current_id = counter[0]
        counter[0] += 1

        # Labeling
        if is_terminal:
            label = node.getText()
        else:
            if rule_name in NICE_NAMES:
                label = NICE_NAMES[rule_name]
            else:
                label = rule_name[0:].capitalize()
                # Remove 'Context' or 'Statement' suffixes if they appear in raw names (usually they don't in ruleNames)
                if label.endswith('Statement'):
                    label = label[:-9]

        G.add_node(current_id)
        labels[current_id] = label
        node_colors[current_id] = get_color(label, is_terminal)

        if parent_id is not None:
            G.add_edge(parent_id, current_id)

        # Recurse
        if not is_terminal:
            for i in range(node.getChildCount()):
                simplify_walk(node.getChild(i), current_id)

        return current_id

    simplify_walk(tree)
    final_colors = [node_colors.get(n, '#ffffff') for n in G.nodes()]
    return G, labels, final_colors

def draw_tree(code, filename, rule_name="program"):
    input_stream = InputStream(code)
    lexer = GGCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GGCodeParser(stream)

    if rule_name == "statement":
        tree = parser.statement()
    else:
        tree = parser.program()

    G, labels, colors = build_graph(tree, parser)

    # Custom layout tweaking
    pos = hierarchy_pos(G, 0, width=2.5, vert_gap=0.2)

    plt.figure(figsize=(10, 6))

    nx.draw_networkx_edges(G, pos, edge_color='#888888', width=1.5, arrows=False)

    # Draw nodes with borders
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color=colors, edgecolors='#444444', linewidths=1.0)

    # Draw labels
    # Wrap long labels if needed, but ours are short
    nx.draw_networkx_labels(G, pos, labels, font_size=9, font_weight='bold', font_family='sans-serif')

    plt.axis('off') # Turn off axis

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images', filename)
    print(f"Saving to {output_path}")
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # 1. Loop
    loop_code = "Repeat 3 times { Move to X10 }"
    try:
        draw_tree(loop_code, "derivation_loop.png", rule_name="statement")
    except Exception as e:
        print(f"Error drawing loop: {e}")

    # 2. Conditional
    cond_code = "If 1 < 2 then { Move to X0 }"
    try:
        draw_tree(cond_code, "derivation_conditional.png", rule_name="statement")
    except Exception as e:
        print(f"Error drawing conditional: {e}")

    # 3. Definition
    def_code = "Define p1 as 10 20"
    try:
        draw_tree(def_code, "derivation_definition.png", rule_name="statement")
    except Exception as e:
        print(f"Error drawing definition: {e}")

    # 4. Assignment
    set_code = "Set s to 100"
    try:
        draw_tree(set_code, "derivation_assignment.png", rule_name="statement")
    except Exception as e:
        print(f"Error drawing assignment: {e}")





