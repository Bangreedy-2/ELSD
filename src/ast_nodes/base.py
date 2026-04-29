from dataclasses import dataclass

@dataclass
class ASTNode:
    line: int
    column: int

from typing import Optional, List, Any
