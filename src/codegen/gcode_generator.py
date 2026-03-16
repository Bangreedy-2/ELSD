from typing import List, Any
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    Statement, VariableDeclaration, Assignment, Block, MoveStatement, IfStatement, RepeatStatement,
    TemperatureStatement, PauseStatement, StopStatement, WaitStatement, SetStatement, AddShapeStatement
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
            if stmt.target:
                t = stmt.target
                if isinstance(t, dict):
                    if t['type'] == 'axis_pair':
                        # Parse X10 Y20
                        # simplistic parsing
                        vals = t['values']
                        self.gcode_lines.append(f"G1 {vals[0]} {vals[1]}")
                    elif t['type'] == 'point' and t['name'].lower() == 'origin':
                        self.gcode_lines.append("G1 X0 Y0")
                    elif t['type'] == 'point':
                        self.gcode_lines.append(f"; Move to {t['name']} (unresolved)")
                    elif t['type'] == 'named':
                        self.gcode_lines.append(f"; Move to user location {t['name']}")
            else:
                # Fallback for old style
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
        elif isinstance(stmt, TemperatureStatement):
             val = self.evaluate(stmt.value)
             self.gcode_lines.append(f"M104 S{val} ; Set Temp")
        elif isinstance(stmt, PauseStatement):
             layer = self.evaluate(stmt.layer)
             self.gcode_lines.append(f"; PAUSE AT LAYER {layer}")
             self.gcode_lines.append("M0") # Marlin pause
        elif isinstance(stmt, StopStatement):
             self.gcode_lines.append("; STOP")
             self.gcode_lines.append("M0")
        elif isinstance(stmt, WaitStatement):
             dur = self.evaluate(stmt.duration)
             seconds = dur if stmt.unit == "seconds" else dur * 60
             self.gcode_lines.append(f"G4 S{seconds} ; Wait")
        elif isinstance(stmt, SetStatement):
             val = self.evaluate(stmt.expression)
             self.env[stmt.identifier] = val
             self.gcode_lines.append(f"; Set {stmt.identifier} = {val}")
        elif isinstance(stmt, AddShapeStatement):
             self.gcode_lines.append(f"; Add Shape {stmt.shape_type}")
             # Generate geometric path (simplified)
             if stmt.shape_type == "square":
                 params = stmt.params
                 center = params.get("center", [0,0])
                 length = params.get("length", 10)
                 cx, cy = center
                 half = length / 2
                 self.gcode_lines.append(f"; Square Center {cx},{cy} Size {length}")
                 # Move to corners
                 self.gcode_lines.append(f"G0 X{cx-half} Y{cy-half}")
                 self.gcode_lines.append(f"G1 X{cx+half} Y{cy-half}")
                 self.gcode_lines.append(f"G1 X{cx+half} Y{cy+half}")
                 self.gcode_lines.append(f"G1 X{cx-half} Y{cy+half}")
                 self.gcode_lines.append(f"G1 X{cx-half} Y{cy-half}")

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

