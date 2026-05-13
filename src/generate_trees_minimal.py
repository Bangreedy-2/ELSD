import sys
import os
import networkx as nx
import matplotlib
matplotlib.use('Agg') # Set backend before importing pyplot
import matplotlib.pyplot as plt
from antlr4 import InputStream, CommonTokenStream, ParserRuleContext, TerminalNode
import traceback

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.antlr_gen.GGCodeLexer import GGCodeLexer
from src.antlr_gen.GGCodeParser import GGCodeParser

def build_graph(tree, parser):
    G = nx.DiGraph()
    labels = {}
    is_terminal_map = {}
    ordered_terminals = []

    counter = [0]

    # Flattening rules
    SKIP_RULES_SINGLE_CHILD = {
        'statement', 'simpleStatement', 'compoundStatement',
        'motionStatement', 'machineStatement', 'geometryStatement', 'definitionStatement',
        'moveTarget', 'coordinateTarget',
        'expression', 'primaryExpression',
        'unaryExpression', 'multiplicativeExpression', 'additiveExpression',
        'numericValue', 'blockStatement', 'locationDefinition',
        'axisSingle', 'centerClause', 'lengthClause', 'widthClause', 'radiusClause',
        'shapeStatement', 'addStatement'
    }

    SKIP_NODE_PROCESS_CHILDREN = {
        'comparisonTail', 'additiveTail', 'multiplicativeTail'
    }

    NICE_NAMES = {
        'repeatStatement': 'Repeat',
        'conditionalStatement': 'If',
        'moveStatement': 'Move',
        'defineStatement': 'Define',
        'setStatement': 'Set',
        'statementList': 'Block',
        'repeatCount': 'Count',
        'condition': 'Cond',
        'statement': 'Stmt',
        'blockStatement': 'Block',
        'coordinatePair': 'Coord',
        'pointTarget': 'Point',
        'axisSingle': 'Axis',
        'numericValue': 'Num',
        'program': 'Program',
        'addStatement': 'Add',
        'squareStatement': 'Square',
        'circleStatement': 'Circle',
        'lineStatement': 'Line',
        'rectangleStatement': 'Rect',
        'squareParameters': 'Params',
        'centerClause': 'Center',
        'lengthClause': 'Length',
        'comparisonExpression': 'Expr',
        'additiveExpression': 'Add-Expr',
        'multiplicativeExpression': 'Mul-Expr',
        'unaryExpression': 'Unary',
        'primaryExpression': 'Expr',
        'locationDefinition': 'Loc'
    }

    def simplify_walk(node, parent_id=None):
        is_terminal = isinstance(node, TerminalNode)

        rule_name = ""
        if not is_terminal:
            rule_index = node.getRuleIndex()
            rule_name = parser.ruleNames[rule_index]

        if node.getText() == "":
            return None

        if not is_terminal and rule_name in SKIP_RULES_SINGLE_CHILD and node.getChildCount() == 1:
            return simplify_walk(node.getChild(0), parent_id)

        if not is_terminal and rule_name in SKIP_NODE_PROCESS_CHILDREN:
            for i in range(node.getChildCount()):
                simplify_walk(node.getChild(i), parent_id)
            return None

        current_id = counter[0]
        counter[0] += 1

        if is_terminal:
            label = node.getText()
            ordered_terminals.append(current_id)
        else:
            if rule_name in NICE_NAMES:
                label = NICE_NAMES[rule_name]
            else:
                label = rule_name[0:].capitalize()
                if label.endswith('Statement'):
                    label = label[:-9]
                if label.endswith('Expression'):
                    label = "Expr"

        G.add_node(current_id)
        labels[current_id] = label
        is_terminal_map[current_id] = is_terminal

        if parent_id is not None:
            G.add_edge(parent_id, current_id)

        if not is_terminal:
            for i in range(node.getChildCount()):
                simplify_walk(node.getChild(i), current_id)

        return current_id

    root_id = simplify_walk(tree)
    # Check if root_id is None (empty tree?)
    return G, labels, is_terminal_map, ordered_terminals, root_id

def calculate_sentence_layout(G, labels, ordered_terminals, root_id):
    pos = {}

    # 1. Position Terminals along the X axis
    current_x = 0.0
    for node_id in ordered_terminals:
        text = labels[node_id]
        # Better visual width estimation
        # Assume monospaced font ~0.6 width per char, plus padding
        width = len(text) * 0.5 + 2.0

        center_x = current_x + width / 2.0
        # Store Y as 0 provisionally
        pos[node_id] = [center_x, 0]
        current_x += width

    # 2. Bubble up X and Assign Y Depth
    if root_id is None:
        try:
            root_id = [n for n, d in G.in_degree() if d == 0][0]
        except IndexError:
            return {}, 10, 0

    try:
        lengths = nx.shortest_path_length(G, source=root_id)
    except Exception:
        # Fallback if graph is weird (e.g. disconnected)
        return nx.spring_layout(G), 10.0, -5.0

    if not lengths:
        max_depth = 0
    else:
        max_depth = max(lengths.values())

    # Process nodes by depth descending (leaves up to root)
    nodes_by_depth = sorted(lengths.keys(), key=lambda x: lengths[x], reverse=True)

    for node in nodes_by_depth:
        # Y is consistently negative depth
        y_pos = -lengths[node]

        if node in ordered_terminals:
            # X is set, Y is -depth
            pos[node][1] = y_pos
        else:
            children = list(G.successors(node))
            if children:
                # Parent X is average of children
                # Filter out children that have no position set (shouldn't happen in tree)
                valid_children = [c for c in children if c in pos]
                if valid_children:
                    avg_x = sum(pos[c][0] for c in valid_children) / len(valid_children)
                    pos[node] = [avg_x, y_pos]
                else:
                    pos[node] = [0, y_pos] # Should not happen
            else:
                 # No children and not marked as terminal? (Empty Block?)
                 # Just give it some X
                 pos[node] = [current_x, y_pos]
                 current_x += 2.0

    return pos, current_x, -max_depth

def draw_tree(code, filename, rule_name="program"):
    try:
        input_stream = InputStream(code)
        lexer = GGCodeLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = GGCodeParser(stream)
        parser.removeErrorListeners()

        if rule_name == "statement":
            tree = parser.statement()
        else:
            tree = parser.program()

        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"Syntax Errors in {filename}")
            return

        G, labels, is_terminal_map, ordered_terminals, root_id = build_graph(tree, parser)

        if G.number_of_nodes() == 0:
            return

        pos, total_width, min_y = calculate_sentence_layout(G, labels, ordered_terminals, root_id)

        # Determine sentence line Y (Below tree)
        sentence_y = min_y - 1.5

        # Figure size
        fig_width = max(8, total_width * 0.4)
        fig_height = abs(min_y) * 1.5 + 3.0

        plt.figure(figsize=(fig_width, fig_height))
        # Set aspect ratio equal to coordinate system so lines are straight 45 degrees relative to grid? No.
        # Just ensure limits are correct.

        non_terminal_nodes = [n for n in G.nodes() if not is_terminal_map[n]]
        terminal_nodes = [n for n in G.nodes() if is_terminal_map[n]]

        # 1. Draw Dotted Lines to Sentence (First, so text overlays)
        for t_node in ordered_terminals:
            if t_node in pos:
                x, y = pos[t_node]
                # Draw from (x, y) to (x, sentence_y)
                # Dotted line
                plt.plot([x, x], [y, sentence_y], color='#555555', linestyle=':', linewidth=1.5, zorder=1)

                # Draw duplicated text at bottom
                text = labels[t_node]
                plt.text(x, sentence_y, text, size=16, ha='center', va='center', fontfamily='monospace', weight='bold',
                         bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=1.0), zorder=3)

        # 2. Draw Tree Edges
        for u, v in G.edges():
            if u in pos and v in pos:
                ux, uy = pos[u]
                vx, vy = pos[v]
                # Simple straight lines
                plt.plot([ux, vx], [uy, vy], color='black', linewidth=1.2, zorder=1)

        # 3. Draw Tree Labels
        # Non-Terminals
        for n in non_terminal_nodes:
            if n in pos:
                x, y = pos[n]
                # White bbox critical to hide lines behind text
                plt.text(x, y, labels[n], size=14, ha='center', va='center', fontfamily='serif',
                         bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=1.0), zorder=2)

        # Terminals (Leaves of Tree)
        for n in terminal_nodes:
            if n in pos:
                x, y = pos[n]
                plt.text(x, y, labels[n], size=14, ha='center', va='center', fontfamily='monospace', weight='bold',
                         bbox=dict(boxstyle="square,pad=0.2", fc="white", ec="none", alpha=1.0), zorder=2)

        # Adjust limits manually to ensure everything fits
        plt.xlim(-1.0, total_width + 1.0)
        plt.ylim(sentence_y - 1.0, 1.0)

        plt.axis('off')

        output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images', filename)
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close('all')
        print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Failed {filename}: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    if not os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images')):
        os.makedirs(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images'))

    # 1. Loop with multiple statements (Block logic)
    draw_tree("Repeat 2 times { Move to X0 Move to Y10 }", "derivation_loop.png", rule_name="statement")

    # 2. Conditional with Else clause
    draw_tree("If 1 < 2 then { Move to X0 } else { Stop at 0mm }", "derivation_conditional.png", rule_name="statement")

    # 3. Definition with descriptive name
    draw_tree("Define safe_pos as 50 50", "derivation_definition.png", rule_name="statement")

    # 4. Assignment with Expression
    draw_tree("Set speed to 100 + 50", "derivation_assignment.png", rule_name="statement")

