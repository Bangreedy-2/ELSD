from typing import Any
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    Statement, VariableDeclaration, Assignment, Block, MoveStatement, IfStatement, RepeatStatement,
    StopStatement, PauseStatement, TemperatureStatement, WaitStatement, UseStatement, DefineStatement,
    SetStatement, AddShapeStatement, RawGCode, AtBlockStatement, Anchor
)
from src.ast_nodes.expressions import (
    Expression, BinaryExpression, UnaryExpression, Literal, Identifier
)
from src.semantic.symbol_table import SymbolTable
from src.semantic.semantic_errors import SemanticError

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, node: Any):
        if isinstance(node, Program):
            self.visit_program(node)
        elif isinstance(node, VariableDeclaration):
            self.visit_variable_declaration(node)
        elif isinstance(node, Assignment):
            self.visit_assignment(node)
        elif isinstance(node, Block):
            self.visit_block(node)
        elif isinstance(node, MoveStatement):
            self.visit_move_statement(node)
        elif isinstance(node, IfStatement):
            self.visit_if_statement(node)
        elif isinstance(node, RepeatStatement):
            self.visit_repeat_statement(node)
        # New Nodes
        elif isinstance(node, DefineStatement):
            self.visit_define_statement(node)
        elif isinstance(node, SetStatement):
            self.visit_set_statement(node)
        elif isinstance(node, TemperatureStatement):
            self.visit_temperature_statement(node)
        elif isinstance(node, WaitStatement):
            self.visit_wait_statement(node)
        elif isinstance(node, AddShapeStatement):
            self.visit_add_shape_statement(node)
        elif isinstance(node, AtBlockStatement):
            self.visit_at_block_statement(node)
        elif isinstance(node, PauseStatement):
            self._validate_anchor(node.anchor, node)
        elif isinstance(node, RawGCode):
            pass # Verbatim passthrough — opaque to semantic analysis
        elif isinstance(node, (StopStatement, UseStatement)):
            pass # No deep validation yet
        # Expressions
        elif isinstance(node, BinaryExpression):
            self.visit_binary_expression(node)
        elif isinstance(node, UnaryExpression):
            self.visit_unary_expression(node)
        elif isinstance(node, Literal):
            pass
        elif isinstance(node, Identifier):
            self.visit_identifier(node)
        else:
             pass

    def visit_program(self, node: Program):
        for stmt in node.statements:
            self.analyze(stmt)

    # Legacy node handling (parsed as Define/Set now?)
    # The grammar removed 'VariableDeclaration' as a rule,
    # but ASTBuilder emits VariableDeclaration? No, it emits DefineStatement or SetStatement?
    # ASTBuilder.visitVariableDeclaration was removed.
    # ASTBuilder.visitDeclaration calls visitDefine or visitSet?
    # No, it calls visitStatement -> simpleStatement -> definitionStatement -> define/set.
    # So VariableDeclaration node is UNUSED in new parser.
    # We should support DefineStatement and SetStatement.

    def visit_variable_declaration(self, node: VariableDeclaration):
        # Legacy support if needed
        self.symbol_table.define(node.identifier)
        self.analyze(node.expression)

    def visit_assignment(self, node: Assignment):
        if not self.symbol_table.exists(node.identifier):
            raise SemanticError(f"Variable '{node.identifier}' not declared.", node.line, node.column)
        self.analyze(node.expression)

    def visit_define_statement(self, node: DefineStatement):
        try:
            self.symbol_table.define(node.identifier, node.location)
        except Exception as e:
            raise SemanticError(str(e), node.line, node.column)

    def visit_set_statement(self, node: SetStatement):
        # Check existence? Or define if 'let' is implicit?
        # "Set speed to 1000" implies existing variable or creating new?
        # Usually Set implies assignment.
        # But for DSL flexibility, we might allow auto-viz.
        # Let's enforce declaration for now to be safe, or just allow it.
        # Given "Define" exists for locations, "Set" is likely for variables.
        if not self.symbol_table.exists(node.identifier):
             # Auto-declare for now to support 'Set speed ...' without 'Let speed ...'
             self.symbol_table.define(node.identifier)
        self.analyze(node.expression)

    def visit_block(self, node: Block):
        self.symbol_table.enter_scope()
        try:
            for stmt in node.statements:
                self.analyze(stmt)
        finally:
            self.symbol_table.exit_scope()

    def visit_move_statement(self, node: MoveStatement):
        # Target validation
        if node.target and isinstance(node.target, dict) and node.target['type'] == 'named':
            name = node.target['name']
            if not self.symbol_table.exists(name):
                raise SemanticError(f"Unknown location '{name}'", node.line, node.column)
        # x, y are dummies

    def visit_if_statement(self, node: IfStatement):
        self.analyze(node.condition)
        self.analyze(node.then_branch)
        if node.else_branch:
            self.analyze(node.else_branch)

    def visit_repeat_statement(self, node: RepeatStatement):
        self.analyze(node.count)
        self.analyze(node.body)

    def visit_binary_expression(self, node: BinaryExpression):
        self.analyze(node.left)
        self.analyze(node.right)

    def visit_unary_expression(self, node: UnaryExpression):
        self.analyze(node.operand)

    def visit_identifier(self, node: Identifier):
        if not self.symbol_table.exists(node.name):
            raise SemanticError(f"Variable '{node.name}' used before declaration.", node.line, node.column)

    def visit_temperature_statement(self, node: TemperatureStatement):
        self.analyze(node.value)

    def visit_wait_statement(self, node: WaitStatement):
        self.analyze(node.duration)

    def visit_add_shape_statement(self, node: AddShapeStatement):
        # Validate params
        pass

    def visit_at_block_statement(self, node: AtBlockStatement):
        self._validate_anchor(node.anchor, node)
        self.analyze(node.body)

    def _validate_anchor(self, anchor, node):
        """Validate anchor structure. Existence (does layer/height exist in the
        file?) is checked in codegen, where the resolved layer map is known, and
        surfaced as a warning rather than a hard error."""
        if anchor is None:
            return
        if anchor.kind == "layer" and (anchor.layer is None or anchor.layer < 0):
            raise SemanticError(f"Invalid layer anchor '{anchor.layer}'", node.line, node.column)
        if anchor.kind == "height" and (anchor.height is None or anchor.height <= 0):
            raise SemanticError(f"Invalid height anchor '{anchor.height}'", node.line, node.column)
