# Generated from src/grammar/GGCode.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u00c0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\7\32\u008b\n\32\f\32\16\32\u008e")
        buf.write("\13\32\3\33\6\33\u0091\n\33\r\33\16\33\u0092\3\33\3\33")
        buf.write("\6\33\u0097\n\33\r\33\16\33\u0098\5\33\u009b\n\33\3\34")
        buf.write("\3\34\5\34\u009f\n\34\3\35\6\35\u00a2\n\35\r\35\16\35")
        buf.write("\u00a3\3\35\3\35\3\36\3\36\3\36\3\36\7\36\u00ac\n\36\f")
        buf.write("\36\16\36\u00af\13\36\3\36\3\36\3\37\3\37\3\37\3\37\7")
        buf.write("\37\u00b7\n\37\f\37\16\37\u00ba\13\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\u00b8\2 \3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\4\2\f\f\17\17\2\u00c7\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\3?\3\2\2\2\5C\3\2\2\2\7H\3\2\2\2\tK\3\2")
        buf.write("\2\2\13P\3\2\2\2\rW\3\2\2\2\17\\\3\2\2\2\21b\3\2\2\2\23")
        buf.write("d\3\2\2\2\25f\3\2\2\2\27h\3\2\2\2\31j\3\2\2\2\33l\3\2")
        buf.write("\2\2\35n\3\2\2\2\37p\3\2\2\2!r\3\2\2\2#t\3\2\2\2%v\3\2")
        buf.write("\2\2\'x\3\2\2\2){\3\2\2\2+~\3\2\2\2-\u0080\3\2\2\2/\u0082")
        buf.write("\3\2\2\2\61\u0085\3\2\2\2\63\u0088\3\2\2\2\65\u0090\3")
        buf.write("\2\2\2\67\u009e\3\2\2\29\u00a1\3\2\2\2;\u00a7\3\2\2\2")
        buf.write("=\u00b2\3\2\2\2?@\7n\2\2@A\7g\2\2AB\7v\2\2B\4\3\2\2\2")
        buf.write("CD\7o\2\2DE\7q\2\2EF\7x\2\2FG\7g\2\2G\6\3\2\2\2HI\7k\2")
        buf.write("\2IJ\7h\2\2J\b\3\2\2\2KL\7g\2\2LM\7n\2\2MN\7u\2\2NO\7")
        buf.write("g\2\2O\n\3\2\2\2PQ\7t\2\2QR\7g\2\2RS\7r\2\2ST\7g\2\2T")
        buf.write("U\7c\2\2UV\7v\2\2V\f\3\2\2\2WX\7v\2\2XY\7t\2\2YZ\7w\2")
        buf.write("\2Z[\7g\2\2[\16\3\2\2\2\\]\7h\2\2]^\7c\2\2^_\7n\2\2_`")
        buf.write("\7u\2\2`a\7g\2\2a\20\3\2\2\2bc\7*\2\2c\22\3\2\2\2de\7")
        buf.write("+\2\2e\24\3\2\2\2fg\7}\2\2g\26\3\2\2\2hi\7\177\2\2i\30")
        buf.write("\3\2\2\2jk\7.\2\2k\32\3\2\2\2lm\7=\2\2m\34\3\2\2\2no\7")
        buf.write("?\2\2o\36\3\2\2\2pq\7-\2\2q \3\2\2\2rs\7/\2\2s\"\3\2\2")
        buf.write("\2tu\7,\2\2u$\3\2\2\2vw\7\61\2\2w&\3\2\2\2xy\7?\2\2yz")
        buf.write("\7?\2\2z(\3\2\2\2{|\7#\2\2|}\7?\2\2}*\3\2\2\2~\177\7@")
        buf.write("\2\2\177,\3\2\2\2\u0080\u0081\7>\2\2\u0081.\3\2\2\2\u0082")
        buf.write("\u0083\7@\2\2\u0083\u0084\7?\2\2\u0084\60\3\2\2\2\u0085")
        buf.write("\u0086\7>\2\2\u0086\u0087\7?\2\2\u0087\62\3\2\2\2\u0088")
        buf.write("\u008c\t\2\2\2\u0089\u008b\t\3\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3")
        buf.write("\2\2\2\u008d\64\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0091")
        buf.write("\t\4\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u009a\3\2\2\2")
        buf.write("\u0094\u0096\7\60\2\2\u0095\u0097\t\4\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009b\3\2\2\2\u009a\u0094\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\66\3\2\2\2\u009c\u009f\5\r")
        buf.write("\7\2\u009d\u009f\5\17\b\2\u009e\u009c\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f8\3\2\2\2\u00a0\u00a2\t\5\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\b\35\2")
        buf.write("\2\u00a6:\3\2\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9\7\61")
        buf.write("\2\2\u00a9\u00ad\3\2\2\2\u00aa\u00ac\n\6\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00b0\u00b1\b\36\2\2\u00b1<\3\2\2\2\u00b2\u00b3\7\61")
        buf.write("\2\2\u00b3\u00b4\7,\2\2\u00b4\u00b8\3\2\2\2\u00b5\u00b7")
        buf.write("\13\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7,\2\2\u00bc\u00bd\7")
        buf.write("\61\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b\37\2\2\u00bf")
        buf.write(">\3\2\2\2\13\2\u008c\u0092\u0098\u009a\u009e\u00a3\u00ad")
        buf.write("\u00b8\3\b\2\2")
        return buf.getvalue()


class GGCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LET = 1
    MOVE = 2
    IF = 3
    ELSE = 4
    REPEAT = 5
    TRUE = 6
    FALSE = 7
    LPAREN = 8
    RPAREN = 9
    LBRACE = 10
    RBRACE = 11
    COMMA = 12
    SEMI = 13
    ASSIGN = 14
    PLUS = 15
    MINUS = 16
    STAR = 17
    SLASH = 18
    EQ = 19
    NEQ = 20
    GT = 21
    LT = 22
    GTE = 23
    LTE = 24
    IDENTIFIER = 25
    NUMBER = 26
    BOOLEAN = 27
    WS = 28
    COMMENT = 29
    BLOCK_COMMENT = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'let'", "'move'", "'if'", "'else'", "'repeat'", "'true'", "'false'", 
            "'('", "')'", "'{'", "'}'", "','", "';'", "'='", "'+'", "'-'", 
            "'*'", "'/'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "LET", "MOVE", "IF", "ELSE", "REPEAT", "TRUE", "FALSE", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "COMMA", "SEMI", "ASSIGN", "PLUS", 
            "MINUS", "STAR", "SLASH", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", 
            "IDENTIFIER", "NUMBER", "BOOLEAN", "WS", "COMMENT", "BLOCK_COMMENT" ]

    ruleNames = [ "LET", "MOVE", "IF", "ELSE", "REPEAT", "TRUE", "FALSE", 
                  "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COMMA", "SEMI", 
                  "ASSIGN", "PLUS", "MINUS", "STAR", "SLASH", "EQ", "NEQ", 
                  "GT", "LT", "GTE", "LTE", "IDENTIFIER", "NUMBER", "BOOLEAN", 
                  "WS", "COMMENT", "BLOCK_COMMENT" ]

    grammarFileName = "GGCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


