from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    LET = auto()
    MOVE = auto()
    TO = auto()
    BY = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    REPEAT = auto()
    TRUE = auto()
    FALSE = auto()

    # Identifiers and Literals
    IDENTIFIER = auto()
    NUMBER = auto()     # Integer or Decimal
    STRING = auto()     # String literal (future)

    # Operators
    PLUS = auto()       # +
    MINUS = auto()      # -
    STAR = auto()       # *
    SLASH = auto()      # /
    ASSIGN = auto()     # =

    # Comparison Operators
    EQ = auto()         # ==
    NEQ = auto()        # !=
    LT = auto()         # <
    LTE = auto()        # <=
    GT = auto()         # >
    GTE = auto()        # >=

    # Delimiters
    LPAREN = auto()     # (
    RPAREN = auto()     # )
    LBRACE = auto()     # {
    RBRACE = auto()     # }
    COMMA = auto()      # ,
    SEMICOLON = auto()  # ;

    # Special
    EOF = auto()
    UNKNOWN = auto()

    # Lexer Rules - Expanded
    STOP = auto()
    PAUSE = auto()
    AT = auto()
    LAYER = auto()
    TEMPERATURE = auto()
    ADD = auto()
    SQUARE = auto()
    CENTER = auto()
    LENGTH = auto()
    WIDTH = auto()
    RECTANGLE = auto()
    CIRCLE = auto()
    RADIUS = auto()
    LINE = auto()
    FROM = auto()
    BASE = auto()
    CENTER_POINT = auto()
    ORIGIN = auto()
    SET = auto()
    DEFINE = auto()
    AS = auto()
    TIMES = auto()
    THEN = auto()
    WAIT = auto()
    FOR = auto()
    SECONDS = auto()
    MINUTES = auto()
    USE = auto()

    # Complex Tokens
    MEASURE = auto()
    TEMPERATURE_VALUE = auto()
    AXIS_VALUE = auto()
