from typing import Any
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    Statement, VariableDeclaration, Assignment, Block, MoveStatement, IfStatement, RepeatStatement
)
from src.ast_nodes.expressions import (
    Expression, BinaryExpression, UnaryExpression, Literal, Identifier
)
from src.semantic.symbol_table import SymbolTable
from src.semantic.semantic_errors import SemanticError
from src.lexer.token_types import TokenType

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
        elif isinstance(node, BinaryExpression):
            self.visit_binary_expression(node)
        elif isinstance(node, UnaryExpression):
            self.visit_unary_expression(node)
        elif isinstance(node, Literal):
            pass # Literals are safe
        elif isinstance(node, Identifier):
            self.visit_identifier(node)
        else:
             # Should probably error on unknown node, but for now traverse
             pass

    def visit_program(self, node: Program):
        for stmt in node.statements:
            self.analyze(stmt)

    def visit_variable_declaration(self, node: VariableDeclaration):
        try:
            self.symbol_table.define(node.identifier)
        except Exception as e:
            raise SemanticError(str(e), node.line, node.column)
        self.analyze(node.expression)

    def visit_assignment(self, node: Assignment):
        if not self.symbol_table.exists(node.identifier):
            raise SemanticError(f"Variable '{node.identifier}' not declared.", node.line, node.column)
        self.analyze(node.expression)

    def visit_block(self, node: Block):
        self.symbol_table.enter_scope()
        try:
            for stmt in node.statements:
                self.analyze(stmt)
        finally:
            self.symbol_table.exit_scope()

    def visit_move_statement(self, node: MoveStatement):
        self.analyze(node.x)
        self.analyze(node.y)

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

