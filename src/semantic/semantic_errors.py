class SemanticError(Exception):
    def __init__(self, message: str, line: int = 0, column: int = 0):
        super().__init__(f"SemanticError: {message} at line {line}, column {column}")
        self.message = message
        self.line = line
        self.column = column

