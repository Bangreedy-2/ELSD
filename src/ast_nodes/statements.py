from dataclasses import dataclass
from typing import List, Optional
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
    x: Expression
    y: Expression

@dataclass
class IfStatement(Statement):
    condition: Expression
    then_branch: Block
    else_branch: Optional[Block] = None

@dataclass
class RepeatStatement(Statement):
    count: Expression
    body: Block

