from dataclasses import dataclass
from typing import List
from src.ast_nodes.base import ASTNode
from src.ast_nodes.statements import Statement

@dataclass
class Program(ASTNode):
    statements: List[Statement]

