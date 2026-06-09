from typing import List, Any, Optional
import math
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    Statement, VariableDeclaration, Assignment, Block, MoveStatement, IfStatement, RepeatStatement,
    TemperatureStatement, PauseStatement, StopStatement, WaitStatement, SetStatement, AddShapeStatement,
    WhileStatement, HomeStatement, RawGCode, AtBlockStatement
)
from src.ast_nodes.expressions import (
    Expression, BinaryExpression, UnaryExpression, Literal, Identifier
)
from src.lexer.token_types import TokenType

class GCodeGenerator:
    def __init__(self, geometry_mode: str = "segmented"):
        self.gcode_lines: List[str] = []
        self.geometry_mode = geometry_mode # "segmented" or "exact" (G2/G3)
        self.env: dict[str, Any] = {}
        # Layer / height tracking
        self.layer_height: float = 0.2   # default layer height in mm
        self.current_layer: int = 0
        self.current_z: float = 0.0

    def _track_z_move(self, axis_value: str):
        """Detect Z moves and emit layer annotation comments."""
        if axis_value.upper().startswith('Z'):
            try:
                z_val = float(axis_value[1:])
                self.current_z = z_val
                if self.layer_height > 0:
                    layer_num = round(z_val / self.layer_height)
                    if layer_num > 0:
                        self.current_layer = layer_num
                        self.gcode_lines.append(
                            f"; === Layer {layer_num} "
                            f"(Z={z_val:.3f}mm, height={self.layer_height}mm) ==="
                        )
            except ValueError:
                pass

    def generate(self, node: Program, layer_map: Optional[dict] = None) -> str:
        self.gcode_lines = []
        self.layer_map = layer_map or {}
        self.visit_program(node)
        return "\n".join(self.gcode_lines)

    def visit_program(self, node: Program):
        self.gcode_lines.append("; Start of GG-Code Program")
        for stmt in node.statements:
            self.visit_statement(stmt)
        self.gcode_lines.append("; End of Program")

    def visit_statement(self, stmt: Statement):
        if isinstance(stmt, RawGCode):
            # Verbatim passthrough — emit exactly as written, no reformatting.
            self.gcode_lines.append(stmt.text)
            if stmt.is_layer_marker:
                self.current_layer = stmt.layer
                self.current_z = stmt.z
                # Friendly navigation annotation (hybrid representation).
                self.gcode_lines.append(f"; >> Layer {stmt.layer} (Z={stmt.z:.3f}mm)")
            return
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
                    elif t['type'] == 'axis_single':
                        vals = t['values']
                        self.gcode_lines.append(f"G1 {vals[0]}")
                        self._track_z_move(vals[0])
                    elif t['type'] == 'axis_triplet':
                        vals = t['values']
                        self.gcode_lines.append(f"G1 {vals[0]} {vals[1]} {vals[2]}")
                        for v in vals:
                            self._track_z_move(v)
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
        elif isinstance(stmt, WhileStatement):
             self.gcode_lines.append(f"; WHILE LOOP")
             self.gcode_lines.append(f"; NOTE: Dynamic while loops are not fully supported in static G-code generation.")
             self.gcode_lines.append(f"; Body will be generated once for demonstration.")
             self.visit_statement(stmt.body)
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
             # Anchored pauses are injected in the two-pass phase (Step 3);
             # an unanchored pause emits inline at the current point.
             if stmt.anchor is None:
                 self.gcode_lines.append("; PAUSE")
                 self.gcode_lines.append("M0") # Marlin pause
        elif isinstance(stmt, StopStatement):
             self.gcode_lines.append("; STOP")
             self.gcode_lines.append("M0")
        elif isinstance(stmt, HomeStatement):
             if not stmt.axes:
                 self.gcode_lines.append("G28 ; Home All")
             else:
                 # G28 X Y means "Home X and Y"
                 # Usually G28 X0 Y0 is safer in some firmwares, but G28 X Y is standard Marlin for "include strictly these"
                 # Actually G28 X0 sets the flag to home X.
                 axes_str = " ".join([f"{axis}0" for axis in stmt.axes])
                 self.gcode_lines.append(f"G28 {axes_str} ; Home {', '.join(stmt.axes)}")
        elif isinstance(stmt, WaitStatement):
             dur = self.evaluate(stmt.duration)
             seconds = dur if stmt.unit == "seconds" else dur * 60
             self.gcode_lines.append(f"G4 S{seconds} ; Wait")
        elif isinstance(stmt, SetStatement):
             val = self.evaluate(stmt.expression)
             self.env[stmt.identifier] = val
             self.gcode_lines.append(f"; Set {stmt.identifier} = {val}")

             # Handle special variables that map to G-code commands
             if stmt.identifier.lower() in ["speed", "feedrate"]:
                 self.gcode_lines.append(f"G1 F{val} ; Set Feedrate")
             elif stmt.identifier.lower() == "layer_height":
                 self.layer_height = float(val)
                 self.gcode_lines.append(f"; Layer height configured: {val}mm per layer")
        elif isinstance(stmt, AddShapeStatement):
             self.gcode_lines.append(f"; Add Shape {stmt.shape_type}")
             params = stmt.params

             if stmt.shape_type == "square":
                 self._generate_rectangle(params.get("center", [0,0]), params.get("length", 10), params.get("length", 10))
             elif stmt.shape_type == "rectangle":
                 self._generate_rectangle(params.get("center", [0,0]), params.get("width", 10), params.get("length", 10))
             elif stmt.shape_type == "circle":
                 self._generate_circle(params.get("center", [0,0]), params.get("radius", 10))
             elif stmt.shape_type == "line":
                 p1 = params.get("from", [0,0])
                 p2 = params.get("to", [0,0])
                 self.gcode_lines.append(f"G0 X{p1[0]} Y{p1[1]}")
                 self.gcode_lines.append(f"G1 X{p2[0]} Y{p2[1]}")

    def _generate_rectangle(self, center, width, length):
        cx, cy = center
        half_w = width / 2
        half_l = length / 2
        # Move to first corner (top-left relative to center, or typical winding)
        # Standard: Bottom-Left -> Bottom-Right -> Top-Right -> Top-Left -> Bottom-Left
        x_min, x_max = cx - half_w, cx + half_w
        y_min, y_max = cy - half_l, cy + half_l

        self.gcode_lines.append(f"G0 X{x_min} Y{y_min}") # Start
        self.gcode_lines.append(f"G1 X{x_max} Y{y_min}")
        self.gcode_lines.append(f"G1 X{x_max} Y{y_max}")
        self.gcode_lines.append(f"G1 X{x_min} Y{y_max}")
        self.gcode_lines.append(f"G1 X{x_min} Y{y_min}") # Close loop

    def _generate_circle(self, center, radius):
        cx, cy = center
        if self.geometry_mode == "exact":
            # Move to start point (rightmost point on circle)
            start_x = cx + radius
            start_y = cy
            self.gcode_lines.append(f"G0 X{start_x} Y{start_y}")
            # G2 X Y I J (Clockwise arc)
            # Full circle usually requires splitting into two semicircles or using specific controller support
            # We'll emit full circle command assuming controller support or split it.
            # I is offset to center in X, J is offset to center in Y
            # From start (cx+r, cy), center is at (-r, 0) relative
            self.gcode_lines.append(f"G2 X{start_x} Y{start_y} I{-radius} J0 ; Full Circle")
        else:
            # Segmented approximation
            segments = 32 # Resolution
            self.gcode_lines.append(f"; Circle Segmented (N={segments})")
            for i in range(segments + 1):
                angle = 2 * math.pi * i / segments
                x = cx + radius * math.cos(angle)
                y = cy + radius * math.sin(angle)
                if i == 0:
                    self.gcode_lines.append(f"G0 X{x:.3f} Y{y:.3f}")
                else:
                    self.gcode_lines.append(f"G1 X{x:.3f} Y{y:.3f}")

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

