from typing import List, Any
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    Statement, VariableDeclaration, Assignment, Block, MoveStatement, IfStatement, RepeatStatement
)
from src.ast_nodes.expressions import (
    Expression, BinaryExpression, UnaryExpression, Literal, Identifier
)
from src.lexer.token_types import TokenType

class GCodeGenerator:
    def __init__(self):
        self.gcode_lines: List[str] = []
        # For simple evaluation if needed, though usually semantic analysis handled symbols
        # Ideally, we need to evaluate expressions to generate concrete G-code coords
        # or propagate variables.
        # For this minimal version, we will try to evaluate simplistic expressions if possible,
        # otherwise we might fail if we encounter unresolved variables in move args
        # (unless we implement a small evaluator here)
        self.env: dict[str, Any] = {}

    def generate(self, node: Program) -> str:
        self.gcode_lines = []
        self.visit_program(node)
        return "\n".join(self.gcode_lines)

    def visit_program(self, node: Program):
        self.gcode_lines.append("; Start of GG-Code Program")
        for stmt in node.statements:
            self.visit_statement(stmt)
        self.gcode_lines.append("; End of Program")

    def visit_statement(self, stmt: Statement):
        if isinstance(stmt, VariableDeclaration):
            val = self.evaluate(stmt.expression)
            self.env[stmt.identifier] = val
            self.gcode_lines.append(f"; Variable declare: {stmt.identifier} = {val}")
        elif isinstance(stmt, Assignment):
            val = self.evaluate(stmt.expression)
            self.env[stmt.identifier] = val
            self.gcode_lines.append(f"; Variable assign: {stmt.identifier} = {val}")
        elif isinstance(stmt, MoveStatement):
            x = self.evaluate(stmt.x)
            y = self.evaluate(stmt.y)
            self.gcode_lines.append(f"G1 X{x} Y{y}")
        elif isinstance(stmt, Block):
            for s in stmt.statements:
                self.visit_statement(s)
        elif isinstance(stmt, RepeatStatement):
             count = self.evaluate(stmt.count)
             self.gcode_lines.append(f"; REPEAT {count} TIMES")
             # Evaluating 'count' times
             if isinstance(count, int) or isinstance(count, float):
                 for i in range(int(count)):
                     self.visit_statement(stmt.body)
             else:
                 self.gcode_lines.append(f"; WARNING: loop count not static cannot unroll")
        elif isinstance(stmt, IfStatement):
             # Static eval for now
             cond = self.evaluate(stmt.condition)
             self.gcode_lines.append(f"; IF CONDITION: {cond}")
             if cond:
                 self.visit_statement(stmt.then_branch)
             elif stmt.else_branch:
                 self.visit_statement(stmt.else_branch)

    def evaluate(self, expr: Expression) -> Any:
        if isinstance(expr, Literal):
            return expr.value
        if isinstance(expr, Identifier):
            return self.env.get(expr.name, 0) # Default to 0 if not found, or error
        if isinstance(expr, BinaryExpression):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            if expr.operator == TokenType.PLUS: return left + right
            if expr.operator == TokenType.MINUS: return left - right
            if expr.operator == TokenType.STAR: return left * right
            if expr.operator == TokenType.SLASH: return left / right
            if expr.operator == TokenType.GT: return left > right
            if expr.operator == TokenType.LT: return left < right
            # ... other ops ...
            return 0
        return 0

