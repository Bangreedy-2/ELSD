from dataclasses import dataclass
from typing import Any, List, Optional
from src.ast_nodes.base import ASTNode
from src.ast_nodes.expressions import Expression

@dataclass
class Statement(ASTNode):
    pass

@dataclass
class VariableDeclaration(Statement):
    identifier: str
    expression: Expression

@dataclass
class Assignment(Statement):
    identifier: str
    expression: Expression

@dataclass
class Block(Statement):
    statements: List[Statement]

@dataclass
class MoveStatement(Statement):
    x: Expression # Deprecated/Placeholder
    y: Expression # Deprecated/Placeholder
    target: Any = None # New flexible target

@dataclass
class IfStatement(Statement):
    condition: Expression
    then_branch: Block
    else_branch: Optional[Block] = None

@dataclass
class RepeatStatement(Statement):
    count: Expression
    body: Block

@dataclass
class WhileStatement(Statement):
    condition: Expression
    body: Block

@dataclass
class StopStatement(Statement):
    measure: Expression # Could be null/literal

@dataclass
class HomeStatement(Statement):
    axes: List[str] # ['X', 'Y', 'Z'] or empty for all

@dataclass
class Anchor:
    """A position anchor: either a layer number or a height in mm."""
    kind: str                          # 'layer' | 'height'
    layer: Optional[int] = None
    height: Optional[float] = None     # mm

@dataclass
class PauseStatement(Statement):
    anchor: Optional[Anchor] = None    # None => pause inline at current point

@dataclass
class AtBlockStatement(Statement):
    """`At layer N { ... }` / `At height H { ... }` — body injected at the anchor."""
    anchor: Anchor
    body: Block

@dataclass
class RawGCode(Statement):
    """A verbatim run of one or more raw G-code / comment lines (passthrough)."""
    text: str
    layer: Optional[int] = None
    z: Optional[float] = None
    is_layer_marker: bool = False

@dataclass
class TemperatureStatement(Statement):
    value: Expression

@dataclass
class WaitStatement(Statement):
    duration: Expression
    unit: str # 'seconds' or 'minutes'

@dataclass
class UseStatement(Statement):
    tool_name: str

@dataclass
class DefineStatement(Statement):
    identifier: str
    location: Any # Simplify for now

@dataclass
class SetStatement(Statement):
    identifier: str
    expression: Expression

@dataclass
class AddShapeStatement(Statement):
    shape_type: str
    params: dict # Simplification for prototyping
