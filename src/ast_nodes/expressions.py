from dataclasses import dataclass
from typing import Any
from src.ast_nodes.base import ASTNode
from src.lexer.token_types import TokenType

@dataclass
class Expression(ASTNode):
    pass

@dataclass
class BinaryExpression(Expression):
    left: Expression
    operator: TokenType
    right: Expression

@dataclass
class UnaryExpression(Expression):
    operator: TokenType
    operand: Expression

@dataclass
class Literal(Expression):
    value: Any  # Number or Boolean

@dataclass
class Identifier(Expression):
    name: str

