from dataclasses import dataclass

@dataclass(kw_only=True)
class ASTNode:
    line: int = 0
    column: int = 0

from typing import Optional, List, Any
