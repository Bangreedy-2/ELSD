from typing import Any, Dict, Optional

class SymbolTable:
    def __init__(self):
        self.scopes: list[Dict[str, Any]] = [{}]

    def enter_scope(self):
        self.scopes.append({})

    def exit_scope(self):
        self.scopes.pop()

    def define(self, name: str, value: Any = None):
        if name in self.scopes[-1]:
            raise Exception(f"Variable '{name}' already defined in this scope.") # Handler should wrap this
        self.scopes[-1][name] = value

    def lookup(self, name: str) -> Optional[Any]:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name] # In checking phase, we often just need existence, or type info effectively
        return None

    def exists(self, name: str) -> bool:
        for scope in reversed(self.scopes):
            if name in scope:
                return True
        return False

