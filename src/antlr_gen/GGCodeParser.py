# Generated from src/grammar/GGCode.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u0172\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\5\4\u0088\n\4\3\5\3\5\3\5\3\5\5\5\u008e\n")
        buf.write("\5\3\6\3\6\3\6\5\6\u0093\n\6\3\7\3\7\3\7\5\7\u0098\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00a1\n\t\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00a7\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\5\23\u00c7\n\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00d7\n\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u00e4\n\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\5(\u0110\n(\3)\3)\3)\3)\3)\3*\3*\5*\u0119")
        buf.write("\n*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u0126\n,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\5-\u0131\n-\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u0145\n\63\3\64\3\64\3\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\5\65\u014f\n\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u0159\n\67\38\38\38\58\u015e\n8\39\39")
        buf.write("\39\39\39\39\59\u0166\n9\3:\3:\3;\3;\3<\3<\3=\3=\3>\3")
        buf.write(">\3>\2\2?\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2")
        buf.write("\b\3\2\24\26\3\2\66\67\3\2-\62\3\2)*\3\2+,\3\2\678\2\u0152")
        buf.write("\2|\3\2\2\2\4\u0083\3\2\2\2\6\u0087\3\2\2\2\b\u008d\3")
        buf.write("\2\2\2\n\u0092\3\2\2\2\f\u0097\3\2\2\2\16\u0099\3\2\2")
        buf.write("\2\20\u00a0\3\2\2\2\22\u00a6\3\2\2\2\24\u00a8\3\2\2\2")
        buf.write("\26\u00ab\3\2\2\2\30\u00af\3\2\2\2\32\u00b2\3\2\2\2\34")
        buf.write("\u00b6\3\2\2\2\36\u00b8\3\2\2\2 \u00ba\3\2\2\2\"\u00be")
        buf.write("\3\2\2\2$\u00c6\3\2\2\2&\u00c8\3\2\2\2(\u00cb\3\2\2\2")
        buf.write("*\u00cf\3\2\2\2,\u00d6\3\2\2\2.\u00d8\3\2\2\2\60\u00da")
        buf.write("\3\2\2\2\62\u00dc\3\2\2\2\64\u00e3\3\2\2\2\66\u00e5\3")
        buf.write("\2\2\28\u00e8\3\2\2\2:\u00eb\3\2\2\2<\u00f0\3\2\2\2>\u00f4")
        buf.write("\3\2\2\2@\u00f8\3\2\2\2B\u00fb\3\2\2\2D\u00fe\3\2\2\2")
        buf.write("F\u0101\3\2\2\2H\u0104\3\2\2\2J\u0107\3\2\2\2L\u010a\3")
        buf.write("\2\2\2N\u010f\3\2\2\2P\u0111\3\2\2\2R\u0118\3\2\2\2T\u011a")
        buf.write("\3\2\2\2V\u011f\3\2\2\2X\u0130\3\2\2\2Z\u0132\3\2\2\2")
        buf.write("\\\u0134\3\2\2\2^\u0138\3\2\2\2`\u013a\3\2\2\2b\u013c")
        buf.write("\3\2\2\2d\u0144\3\2\2\2f\u0146\3\2\2\2h\u014e\3\2\2\2")
        buf.write("j\u0150\3\2\2\2l\u0158\3\2\2\2n\u015d\3\2\2\2p\u0165\3")
        buf.write("\2\2\2r\u0167\3\2\2\2t\u0169\3\2\2\2v\u016b\3\2\2\2x\u016d")
        buf.write("\3\2\2\2z\u016f\3\2\2\2|}\5\4\3\2}~\7\2\2\3~\3\3\2\2\2")
        buf.write("\177\u0080\5\6\4\2\u0080\u0081\5\4\3\2\u0081\u0084\3\2")
        buf.write("\2\2\u0082\u0084\5\6\4\2\u0083\177\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\5\3\2\2\2\u0085\u0088\5\b\5\2\u0086\u0088")
        buf.write("\5\n\6\2\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\7\3\2\2\2\u0089\u008e\5\f\7\2\u008a\u008e\5$\23\2\u008b")
        buf.write("\u008e\5\60\31\2\u008c\u008e\5N(\2\u008d\u0089\3\2\2\2")
        buf.write("\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c\3")
        buf.write("\2\2\2\u008e\t\3\2\2\2\u008f\u0093\5V,\2\u0090\u0093\5")
        buf.write("X-\2\u0091\u0093\5\\/\2\u0092\u008f\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\13\3\2\2\2\u0094\u0098")
        buf.write("\5\16\b\2\u0095\u0098\5 \21\2\u0096\u0098\5\"\22\2\u0097")
        buf.write("\u0094\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2")
        buf.write("\u0098\r\3\2\2\2\u0099\u009a\7\b\2\2\u009a\u009b\7\t\2")
        buf.write("\2\u009b\u009c\5\20\t\2\u009c\17\3\2\2\2\u009d\u00a1\5")
        buf.write("\22\n\2\u009e\u00a1\5\34\17\2\u009f\u00a1\5\36\20\2\u00a0")
        buf.write("\u009d\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2")
        buf.write("\u00a1\21\3\2\2\2\u00a2\u00a7\5\24\13\2\u00a3\u00a7\5")
        buf.write("\26\f\2\u00a4\u00a7\5\30\r\2\u00a5\u00a7\5\32\16\2\u00a6")
        buf.write("\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\23\3\2\2\2\u00a8\u00a9\7\65")
        buf.write("\2\2\u00a9\u00aa\7\65\2\2\u00aa\25\3\2\2\2\u00ab\u00ac")
        buf.write("\7\65\2\2\u00ac\u00ad\7\65\2\2\u00ad\u00ae\7\65\2\2\u00ae")
        buf.write("\27\3\2\2\2\u00af\u00b0\5z>\2\u00b0\u00b1\5z>\2\u00b1")
        buf.write("\31\3\2\2\2\u00b2\u00b3\5z>\2\u00b3\u00b4\5z>\2\u00b4")
        buf.write("\u00b5\5z>\2\u00b5\33\3\2\2\2\u00b6\u00b7\t\2\2\2\u00b7")
        buf.write("\35\3\2\2\2\u00b8\u00b9\7\66\2\2\u00b9\37\3\2\2\2\u00ba")
        buf.write("\u00bb\7\3\2\2\u00bb\u00bc\7\5\2\2\u00bc\u00bd\5z>\2\u00bd")
        buf.write("!\3\2\2\2\u00be\u00bf\7\4\2\2\u00bf\u00c0\7\5\2\2\u00c0")
        buf.write("\u00c1\7\6\2\2\u00c1\u00c2\7\67\2\2\u00c2#\3\2\2\2\u00c3")
        buf.write("\u00c7\5&\24\2\u00c4\u00c7\5(\25\2\u00c5\u00c7\5*\26\2")
        buf.write("\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3")
        buf.write("\2\2\2\u00c7%\3\2\2\2\u00c8\u00c9\7\7\2\2\u00c9\u00ca")
        buf.write("\5.\30\2\u00ca\'\3\2\2\2\u00cb\u00cc\7 \2\2\u00cc\u00cd")
        buf.write("\7!\2\2\u00cd\u00ce\5,\27\2\u00ce)\3\2\2\2\u00cf\u00d0")
        buf.write("\7$\2\2\u00d0\u00d1\7\66\2\2\u00d1+\3\2\2\2\u00d2\u00d3")
        buf.write("\7\67\2\2\u00d3\u00d7\7\"\2\2\u00d4\u00d5\7\67\2\2\u00d5")
        buf.write("\u00d7\7#\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d7-\3\2\2\2\u00d8\u00d9\7\64\2\2\u00d9/\3\2\2\2\u00da")
        buf.write("\u00db\5\62\32\2\u00db\61\3\2\2\2\u00dc\u00dd\7\n\2\2")
        buf.write("\u00dd\u00de\5\64\33\2\u00de\63\3\2\2\2\u00df\u00e4\5")
        buf.write("\66\34\2\u00e0\u00e4\5:\36\2\u00e1\u00e4\5<\37\2\u00e2")
        buf.write("\u00e4\5> \2\u00e3\u00df\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\65\3\2\2\2\u00e5")
        buf.write("\u00e6\7\13\2\2\u00e6\u00e7\58\35\2\u00e7\67\3\2\2\2\u00e8")
        buf.write("\u00e9\5@!\2\u00e9\u00ea\5D#\2\u00ea9\3\2\2\2\u00eb\u00ec")
        buf.write("\7\17\2\2\u00ec\u00ed\5@!\2\u00ed\u00ee\5B\"\2\u00ee\u00ef")
        buf.write("\5D#\2\u00ef;\3\2\2\2\u00f0\u00f1\7\20\2\2\u00f1\u00f2")
        buf.write("\5@!\2\u00f2\u00f3\5F$\2\u00f3=\3\2\2\2\u00f4\u00f5\7")
        buf.write("\22\2\2\u00f5\u00f6\5H%\2\u00f6\u00f7\5J&\2\u00f7?\3\2")
        buf.write("\2\2\u00f8\u00f9\7\f\2\2\u00f9\u00fa\5L\'\2\u00faA\3\2")
        buf.write("\2\2\u00fb\u00fc\7\16\2\2\u00fc\u00fd\5x=\2\u00fdC\3\2")
        buf.write("\2\2\u00fe\u00ff\7\r\2\2\u00ff\u0100\5x=\2\u0100E\3\2")
        buf.write("\2\2\u0101\u0102\7\21\2\2\u0102\u0103\5x=\2\u0103G\3\2")
        buf.write("\2\2\u0104\u0105\7\23\2\2\u0105\u0106\5L\'\2\u0106I\3")
        buf.write("\2\2\2\u0107\u0108\7\t\2\2\u0108\u0109\5L\'\2\u0109K\3")
        buf.write("\2\2\2\u010a\u010b\5x=\2\u010b\u010c\5x=\2\u010cM\3\2")
        buf.write("\2\2\u010d\u0110\5P)\2\u010e\u0110\5T+\2\u010f\u010d\3")
        buf.write("\2\2\2\u010f\u010e\3\2\2\2\u0110O\3\2\2\2\u0111\u0112")
        buf.write("\7\30\2\2\u0112\u0113\7\66\2\2\u0113\u0114\7\31\2\2\u0114")
        buf.write("\u0115\5R*\2\u0115Q\3\2\2\2\u0116\u0119\5L\'\2\u0117\u0119")
        buf.write("\5\34\17\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119")
        buf.write("S\3\2\2\2\u011a\u011b\7\27\2\2\u011b\u011c\7\66\2\2\u011c")
        buf.write("\u011d\7\t\2\2\u011d\u011e\5`\61\2\u011eU\3\2\2\2\u011f")
        buf.write("\u0120\7\34\2\2\u0120\u0121\5^\60\2\u0121\u0122\7\35\2")
        buf.write("\2\u0122\u0125\5\\/\2\u0123\u0124\7\36\2\2\u0124\u0126")
        buf.write("\5\\/\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("W\3\2\2\2\u0127\u0128\7\32\2\2\u0128\u0129\5Z.\2\u0129")
        buf.write("\u012a\7\33\2\2\u012a\u012b\5\\/\2\u012b\u0131\3\2\2\2")
        buf.write("\u012c\u012d\7\37\2\2\u012d\u012e\5^\60\2\u012e\u012f")
        buf.write("\5\\/\2\u012f\u0131\3\2\2\2\u0130\u0127\3\2\2\2\u0130")
        buf.write("\u012c\3\2\2\2\u0131Y\3\2\2\2\u0132\u0133\t\3\2\2\u0133")
        buf.write("[\3\2\2\2\u0134\u0135\7\'\2\2\u0135\u0136\5\4\3\2\u0136")
        buf.write("\u0137\7(\2\2\u0137]\3\2\2\2\u0138\u0139\5`\61\2\u0139")
        buf.write("_\3\2\2\2\u013a\u013b\5b\62\2\u013ba\3\2\2\2\u013c\u013d")
        buf.write("\5f\64\2\u013d\u013e\5d\63\2\u013ec\3\2\2\2\u013f\u0140")
        buf.write("\5r:\2\u0140\u0141\5f\64\2\u0141\u0142\5d\63\2\u0142\u0145")
        buf.write("\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u013f\3\2\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145e\3\2\2\2\u0146\u0147\5j\66\2\u0147")
        buf.write("\u0148\5h\65\2\u0148g\3\2\2\2\u0149\u014a\5t;\2\u014a")
        buf.write("\u014b\5j\66\2\u014b\u014c\5h\65\2\u014c\u014f\3\2\2\2")
        buf.write("\u014d\u014f\3\2\2\2\u014e\u0149\3\2\2\2\u014e\u014d\3")
        buf.write("\2\2\2\u014fi\3\2\2\2\u0150\u0151\5n8\2\u0151\u0152\5")
        buf.write("l\67\2\u0152k\3\2\2\2\u0153\u0154\5v<\2\u0154\u0155\5")
        buf.write("n8\2\u0155\u0156\5l\67\2\u0156\u0159\3\2\2\2\u0157\u0159")
        buf.write("\3\2\2\2\u0158\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159")
        buf.write("m\3\2\2\2\u015a\u015b\7*\2\2\u015b\u015e\5n8\2\u015c\u015e")
        buf.write("\5p9\2\u015d\u015a\3\2\2\2\u015d\u015c\3\2\2\2\u015eo")
        buf.write("\3\2\2\2\u015f\u0166\5x=\2\u0160\u0166\7\66\2\2\u0161")
        buf.write("\u0162\7%\2\2\u0162\u0163\5`\61\2\u0163\u0164\7&\2\2\u0164")
        buf.write("\u0166\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0160\3\2\2\2")
        buf.write("\u0165\u0161\3\2\2\2\u0166q\3\2\2\2\u0167\u0168\t\4\2")
        buf.write("\2\u0168s\3\2\2\2\u0169\u016a\t\5\2\2\u016au\3\2\2\2\u016b")
        buf.write("\u016c\t\6\2\2\u016cw\3\2\2\2\u016d\u016e\t\7\2\2\u016e")
        buf.write("y\3\2\2\2\u016f\u0170\7\63\2\2\u0170{\3\2\2\2\25\u0083")
        buf.write("\u0087\u008d\u0092\u0097\u00a0\u00a6\u00c6\u00d6\u00e3")
        buf.write("\u010f\u0118\u0125\u0130\u0144\u014e\u0158\u015d\u0165")
        return buf.getvalue()


class GGCodeParser ( Parser ):

    grammarFileName = "GGCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "STOP", "PAUSE", "AT", "LAYER", "TEMPERATURE", 
                      "MOVE", "TO", "ADD", "SQUARE", "CENTER", "LENGTH", 
                      "WIDTH", "RECTANGLE", "CIRCLE", "RADIUS", "LINE", 
                      "FROM", "BASE", "CENTER_POINT", "ORIGIN", "SET", "DEFINE", 
                      "AS", "REPEAT", "TIMES", "IF", "THEN", "ELSE", "WHILE", 
                      "WAIT", "FOR", "SECONDS", "MINUTES", "USE", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", 
                      "SLASH", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "MEASURE", 
                      "TEMPERATURE_VALUE", "AXIS_VALUE", "IDENTIFIER", "INTERGER", 
                      "DECIMAL", "WS", "BLOCK_COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_simpleStatement = 3
    RULE_compoundStatement = 4
    RULE_motionStatement = 5
    RULE_moveStatement = 6
    RULE_moveTarget = 7
    RULE_coordinateTarget = 8
    RULE_axisPair = 9
    RULE_axisTriplet = 10
    RULE_measurePair = 11
    RULE_measureTriplet = 12
    RULE_pointTarget = 13
    RULE_namedTarget = 14
    RULE_stopStatement = 15
    RULE_pauseStatement = 16
    RULE_machineStatement = 17
    RULE_temperatureStatement = 18
    RULE_waitStatement = 19
    RULE_useStatement = 20
    RULE_durationValue = 21
    RULE_temperatureValue = 22
    RULE_geometryStatement = 23
    RULE_addStatement = 24
    RULE_shapeStatement = 25
    RULE_squareStatement = 26
    RULE_squareParameters = 27
    RULE_rectangleStatement = 28
    RULE_circleStatement = 29
    RULE_lineStatement = 30
    RULE_centerClause = 31
    RULE_widthClause = 32
    RULE_lengthClause = 33
    RULE_radiusClause = 34
    RULE_fromClause = 35
    RULE_toClause = 36
    RULE_coordinatePair = 37
    RULE_definitionStatement = 38
    RULE_defineStatement = 39
    RULE_locationDefinition = 40
    RULE_setStatement = 41
    RULE_conditionalStatement = 42
    RULE_loopStatement = 43
    RULE_repeatCount = 44
    RULE_blockStatement = 45
    RULE_condition = 46
    RULE_expression = 47
    RULE_comparisonExpression = 48
    RULE_comparisonTail = 49
    RULE_additiveExpression = 50
    RULE_additiveTail = 51
    RULE_multiplicativeExpression = 52
    RULE_multiplicativeTail = 53
    RULE_unaryExpression = 54
    RULE_primaryExpression = 55
    RULE_comparisonOperator = 56
    RULE_addOperator = 57
    RULE_mulOperator = 58
    RULE_numericValue = 59
    RULE_measure = 60

    ruleNames =  [ "program", "statementList", "statement", "simpleStatement", 
                   "compoundStatement", "motionStatement", "moveStatement", 
                   "moveTarget", "coordinateTarget", "axisPair", "axisTriplet", 
                   "measurePair", "measureTriplet", "pointTarget", "namedTarget", 
                   "stopStatement", "pauseStatement", "machineStatement", 
                   "temperatureStatement", "waitStatement", "useStatement", 
                   "durationValue", "temperatureValue", "geometryStatement", 
                   "addStatement", "shapeStatement", "squareStatement", 
                   "squareParameters", "rectangleStatement", "circleStatement", 
                   "lineStatement", "centerClause", "widthClause", "lengthClause", 
                   "radiusClause", "fromClause", "toClause", "coordinatePair", 
                   "definitionStatement", "defineStatement", "locationDefinition", 
                   "setStatement", "conditionalStatement", "loopStatement", 
                   "repeatCount", "blockStatement", "condition", "expression", 
                   "comparisonExpression", "comparisonTail", "additiveExpression", 
                   "additiveTail", "multiplicativeExpression", "multiplicativeTail", 
                   "unaryExpression", "primaryExpression", "comparisonOperator", 
                   "addOperator", "mulOperator", "numericValue", "measure" ]

    EOF = Token.EOF
    STOP=1
    PAUSE=2
    AT=3
    LAYER=4
    TEMPERATURE=5
    MOVE=6
    TO=7
    ADD=8
    SQUARE=9
    CENTER=10
    LENGTH=11
    WIDTH=12
    RECTANGLE=13
    CIRCLE=14
    RADIUS=15
    LINE=16
    FROM=17
    BASE=18
    CENTER_POINT=19
    ORIGIN=20
    SET=21
    DEFINE=22
    AS=23
    REPEAT=24
    TIMES=25
    IF=26
    THEN=27
    ELSE=28
    WHILE=29
    WAIT=30
    FOR=31
    SECONDS=32
    MINUTES=33
    USE=34
    LPAREN=35
    RPAREN=36
    LBRACE=37
    RBRACE=38
    PLUS=39
    MINUS=40
    STAR=41
    SLASH=42
    EQ=43
    NEQ=44
    GT=45
    LT=46
    GTE=47
    LTE=48
    MEASURE=49
    TEMPERATURE_VALUE=50
    AXIS_VALUE=51
    IDENTIFIER=52
    INTERGER=53
    DECIMAL=54
    WS=55
    BLOCK_COMMENT=56
    LINE_COMMENT=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(GGCodeParser.StatementListContext,0)


        def EOF(self):
            return self.getToken(GGCodeParser.EOF, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GGCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.statementList()
            self.state = 123
            self.match(GGCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(GGCodeParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(GGCodeParser.StatementListContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = GGCodeParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.statement()
                self.state = 126
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStatement(self):
            return self.getTypedRuleContext(GGCodeParser.SimpleStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(GGCodeParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = GGCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.WAIT, GGCodeParser.USE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.simpleStatement()
                pass
            elif token in [GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.WHILE, GGCodeParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.compoundStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def motionStatement(self):
            return self.getTypedRuleContext(GGCodeParser.MotionStatementContext,0)


        def machineStatement(self):
            return self.getTypedRuleContext(GGCodeParser.MachineStatementContext,0)


        def geometryStatement(self):
            return self.getTypedRuleContext(GGCodeParser.GeometryStatementContext,0)


        def definitionStatement(self):
            return self.getTypedRuleContext(GGCodeParser.DefinitionStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_simpleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStatement" ):
                listener.enterSimpleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStatement" ):
                listener.exitSimpleStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStatement" ):
                return visitor.visitSimpleStatement(self)
            else:
                return visitor.visitChildren(self)




    def simpleStatement(self):

        localctx = GGCodeParser.SimpleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simpleStatement)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.MOVE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.motionStatement()
                pass
            elif token in [GGCodeParser.TEMPERATURE, GGCodeParser.WAIT, GGCodeParser.USE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.machineStatement()
                pass
            elif token in [GGCodeParser.ADD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.geometryStatement()
                pass
            elif token in [GGCodeParser.SET, GGCodeParser.DEFINE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.definitionStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalStatement(self):
            return self.getTypedRuleContext(GGCodeParser.ConditionalStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(GGCodeParser.LoopStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(GGCodeParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = GGCodeParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compoundStatement)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.conditionalStatement()
                pass
            elif token in [GGCodeParser.REPEAT, GGCodeParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.loopStatement()
                pass
            elif token in [GGCodeParser.LBRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
                self.blockStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MotionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveStatement(self):
            return self.getTypedRuleContext(GGCodeParser.MoveStatementContext,0)


        def stopStatement(self):
            return self.getTypedRuleContext(GGCodeParser.StopStatementContext,0)


        def pauseStatement(self):
            return self.getTypedRuleContext(GGCodeParser.PauseStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_motionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMotionStatement" ):
                listener.enterMotionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMotionStatement" ):
                listener.exitMotionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMotionStatement" ):
                return visitor.visitMotionStatement(self)
            else:
                return visitor.visitChildren(self)




    def motionStatement(self):

        localctx = GGCodeParser.MotionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_motionStatement)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MOVE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.moveStatement()
                pass
            elif token in [GGCodeParser.STOP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.stopStatement()
                pass
            elif token in [GGCodeParser.PAUSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.pauseStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(GGCodeParser.MOVE, 0)

        def TO(self):
            return self.getToken(GGCodeParser.TO, 0)

        def moveTarget(self):
            return self.getTypedRuleContext(GGCodeParser.MoveTargetContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_moveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveStatement" ):
                listener.enterMoveStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveStatement" ):
                listener.exitMoveStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveStatement" ):
                return visitor.visitMoveStatement(self)
            else:
                return visitor.visitChildren(self)




    def moveStatement(self):

        localctx = GGCodeParser.MoveStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_moveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(GGCodeParser.MOVE)
            self.state = 152
            self.match(GGCodeParser.TO)
            self.state = 153
            self.moveTarget()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordinateTarget(self):
            return self.getTypedRuleContext(GGCodeParser.CoordinateTargetContext,0)


        def pointTarget(self):
            return self.getTypedRuleContext(GGCodeParser.PointTargetContext,0)


        def namedTarget(self):
            return self.getTypedRuleContext(GGCodeParser.NamedTargetContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_moveTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveTarget" ):
                listener.enterMoveTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveTarget" ):
                listener.exitMoveTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveTarget" ):
                return visitor.visitMoveTarget(self)
            else:
                return visitor.visitChildren(self)




    def moveTarget(self):

        localctx = GGCodeParser.MoveTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_moveTarget)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MEASURE, GGCodeParser.AXIS_VALUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.coordinateTarget()
                pass
            elif token in [GGCodeParser.BASE, GGCodeParser.CENTER_POINT, GGCodeParser.ORIGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.pointTarget()
                pass
            elif token in [GGCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.namedTarget()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordinateTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def axisPair(self):
            return self.getTypedRuleContext(GGCodeParser.AxisPairContext,0)


        def axisTriplet(self):
            return self.getTypedRuleContext(GGCodeParser.AxisTripletContext,0)


        def measurePair(self):
            return self.getTypedRuleContext(GGCodeParser.MeasurePairContext,0)


        def measureTriplet(self):
            return self.getTypedRuleContext(GGCodeParser.MeasureTripletContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_coordinateTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordinateTarget" ):
                listener.enterCoordinateTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordinateTarget" ):
                listener.exitCoordinateTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordinateTarget" ):
                return visitor.visitCoordinateTarget(self)
            else:
                return visitor.visitChildren(self)




    def coordinateTarget(self):

        localctx = GGCodeParser.CoordinateTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coordinateTarget)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.axisPair()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.axisTriplet()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.measurePair()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.measureTriplet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisPairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AXIS_VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(GGCodeParser.AXIS_VALUE)
            else:
                return self.getToken(GGCodeParser.AXIS_VALUE, i)

        def getRuleIndex(self):
            return GGCodeParser.RULE_axisPair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxisPair" ):
                listener.enterAxisPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxisPair" ):
                listener.exitAxisPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxisPair" ):
                return visitor.visitAxisPair(self)
            else:
                return visitor.visitChildren(self)




    def axisPair(self):

        localctx = GGCodeParser.AxisPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_axisPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(GGCodeParser.AXIS_VALUE)
            self.state = 167
            self.match(GGCodeParser.AXIS_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisTripletContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AXIS_VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(GGCodeParser.AXIS_VALUE)
            else:
                return self.getToken(GGCodeParser.AXIS_VALUE, i)

        def getRuleIndex(self):
            return GGCodeParser.RULE_axisTriplet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxisTriplet" ):
                listener.enterAxisTriplet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxisTriplet" ):
                listener.exitAxisTriplet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxisTriplet" ):
                return visitor.visitAxisTriplet(self)
            else:
                return visitor.visitChildren(self)




    def axisTriplet(self):

        localctx = GGCodeParser.AxisTripletContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_axisTriplet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GGCodeParser.AXIS_VALUE)
            self.state = 170
            self.match(GGCodeParser.AXIS_VALUE)
            self.state = 171
            self.match(GGCodeParser.AXIS_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasurePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def measure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.MeasureContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.MeasureContext,i)


        def getRuleIndex(self):
            return GGCodeParser.RULE_measurePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasurePair" ):
                listener.enterMeasurePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasurePair" ):
                listener.exitMeasurePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeasurePair" ):
                return visitor.visitMeasurePair(self)
            else:
                return visitor.visitChildren(self)




    def measurePair(self):

        localctx = GGCodeParser.MeasurePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_measurePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.measure()
            self.state = 174
            self.measure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasureTripletContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def measure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.MeasureContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.MeasureContext,i)


        def getRuleIndex(self):
            return GGCodeParser.RULE_measureTriplet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasureTriplet" ):
                listener.enterMeasureTriplet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasureTriplet" ):
                listener.exitMeasureTriplet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeasureTriplet" ):
                return visitor.visitMeasureTriplet(self)
            else:
                return visitor.visitChildren(self)




    def measureTriplet(self):

        localctx = GGCodeParser.MeasureTripletContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_measureTriplet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.measure()
            self.state = 177
            self.measure()
            self.state = 178
            self.measure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BASE(self):
            return self.getToken(GGCodeParser.BASE, 0)

        def CENTER_POINT(self):
            return self.getToken(GGCodeParser.CENTER_POINT, 0)

        def ORIGIN(self):
            return self.getToken(GGCodeParser.ORIGIN, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_pointTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointTarget" ):
                listener.enterPointTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointTarget" ):
                listener.exitPointTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointTarget" ):
                return visitor.visitPointTarget(self)
            else:
                return visitor.visitChildren(self)




    def pointTarget(self):

        localctx = GGCodeParser.PointTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pointTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.BASE) | (1 << GGCodeParser.CENTER_POINT) | (1 << GGCodeParser.ORIGIN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamedTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_namedTarget

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedTarget" ):
                listener.enterNamedTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedTarget" ):
                listener.exitNamedTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedTarget" ):
                return visitor.visitNamedTarget(self)
            else:
                return visitor.visitChildren(self)




    def namedTarget(self):

        localctx = GGCodeParser.NamedTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_namedTarget)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(GGCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOP(self):
            return self.getToken(GGCodeParser.STOP, 0)

        def AT(self):
            return self.getToken(GGCodeParser.AT, 0)

        def measure(self):
            return self.getTypedRuleContext(GGCodeParser.MeasureContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_stopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStopStatement" ):
                listener.enterStopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStopStatement" ):
                listener.exitStopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStopStatement" ):
                return visitor.visitStopStatement(self)
            else:
                return visitor.visitChildren(self)




    def stopStatement(self):

        localctx = GGCodeParser.StopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(GGCodeParser.STOP)
            self.state = 185
            self.match(GGCodeParser.AT)
            self.state = 186
            self.measure()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAUSE(self):
            return self.getToken(GGCodeParser.PAUSE, 0)

        def AT(self):
            return self.getToken(GGCodeParser.AT, 0)

        def LAYER(self):
            return self.getToken(GGCodeParser.LAYER, 0)

        def INTERGER(self):
            return self.getToken(GGCodeParser.INTERGER, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_pauseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPauseStatement" ):
                listener.enterPauseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPauseStatement" ):
                listener.exitPauseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPauseStatement" ):
                return visitor.visitPauseStatement(self)
            else:
                return visitor.visitChildren(self)




    def pauseStatement(self):

        localctx = GGCodeParser.PauseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pauseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(GGCodeParser.PAUSE)
            self.state = 189
            self.match(GGCodeParser.AT)
            self.state = 190
            self.match(GGCodeParser.LAYER)
            self.state = 191
            self.match(GGCodeParser.INTERGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MachineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def temperatureStatement(self):
            return self.getTypedRuleContext(GGCodeParser.TemperatureStatementContext,0)


        def waitStatement(self):
            return self.getTypedRuleContext(GGCodeParser.WaitStatementContext,0)


        def useStatement(self):
            return self.getTypedRuleContext(GGCodeParser.UseStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_machineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMachineStatement" ):
                listener.enterMachineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMachineStatement" ):
                listener.exitMachineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMachineStatement" ):
                return visitor.visitMachineStatement(self)
            else:
                return visitor.visitChildren(self)




    def machineStatement(self):

        localctx = GGCodeParser.MachineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_machineStatement)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.TEMPERATURE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.temperatureStatement()
                pass
            elif token in [GGCodeParser.WAIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.waitStatement()
                pass
            elif token in [GGCodeParser.USE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.useStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemperatureStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPERATURE(self):
            return self.getToken(GGCodeParser.TEMPERATURE, 0)

        def temperatureValue(self):
            return self.getTypedRuleContext(GGCodeParser.TemperatureValueContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_temperatureStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemperatureStatement" ):
                listener.enterTemperatureStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemperatureStatement" ):
                listener.exitTemperatureStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemperatureStatement" ):
                return visitor.visitTemperatureStatement(self)
            else:
                return visitor.visitChildren(self)




    def temperatureStatement(self):

        localctx = GGCodeParser.TemperatureStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_temperatureStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(GGCodeParser.TEMPERATURE)
            self.state = 199
            self.temperatureValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT(self):
            return self.getToken(GGCodeParser.WAIT, 0)

        def FOR(self):
            return self.getToken(GGCodeParser.FOR, 0)

        def durationValue(self):
            return self.getTypedRuleContext(GGCodeParser.DurationValueContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_waitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitStatement" ):
                listener.enterWaitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitStatement" ):
                listener.exitWaitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitStatement" ):
                return visitor.visitWaitStatement(self)
            else:
                return visitor.visitChildren(self)




    def waitStatement(self):

        localctx = GGCodeParser.WaitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_waitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(GGCodeParser.WAIT)
            self.state = 202
            self.match(GGCodeParser.FOR)
            self.state = 203
            self.durationValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(GGCodeParser.USE, 0)

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_useStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseStatement" ):
                listener.enterUseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseStatement" ):
                listener.exitUseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseStatement" ):
                return visitor.visitUseStatement(self)
            else:
                return visitor.visitChildren(self)




    def useStatement(self):

        localctx = GGCodeParser.UseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_useStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(GGCodeParser.USE)
            self.state = 206
            self.match(GGCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DurationValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERGER(self):
            return self.getToken(GGCodeParser.INTERGER, 0)

        def SECONDS(self):
            return self.getToken(GGCodeParser.SECONDS, 0)

        def MINUTES(self):
            return self.getToken(GGCodeParser.MINUTES, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_durationValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDurationValue" ):
                listener.enterDurationValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDurationValue" ):
                listener.exitDurationValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDurationValue" ):
                return visitor.visitDurationValue(self)
            else:
                return visitor.visitChildren(self)




    def durationValue(self):

        localctx = GGCodeParser.DurationValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_durationValue)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(GGCodeParser.INTERGER)
                self.state = 209
                self.match(GGCodeParser.SECONDS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(GGCodeParser.INTERGER)
                self.state = 211
                self.match(GGCodeParser.MINUTES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemperatureValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPERATURE_VALUE(self):
            return self.getToken(GGCodeParser.TEMPERATURE_VALUE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_temperatureValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemperatureValue" ):
                listener.enterTemperatureValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemperatureValue" ):
                listener.exitTemperatureValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemperatureValue" ):
                return visitor.visitTemperatureValue(self)
            else:
                return visitor.visitChildren(self)




    def temperatureValue(self):

        localctx = GGCodeParser.TemperatureValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_temperatureValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(GGCodeParser.TEMPERATURE_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeometryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addStatement(self):
            return self.getTypedRuleContext(GGCodeParser.AddStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_geometryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeometryStatement" ):
                listener.enterGeometryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeometryStatement" ):
                listener.exitGeometryStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeometryStatement" ):
                return visitor.visitGeometryStatement(self)
            else:
                return visitor.visitChildren(self)




    def geometryStatement(self):

        localctx = GGCodeParser.GeometryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_geometryStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.addStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(GGCodeParser.ADD, 0)

        def shapeStatement(self):
            return self.getTypedRuleContext(GGCodeParser.ShapeStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_addStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddStatement" ):
                listener.enterAddStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddStatement" ):
                listener.exitAddStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddStatement" ):
                return visitor.visitAddStatement(self)
            else:
                return visitor.visitChildren(self)




    def addStatement(self):

        localctx = GGCodeParser.AddStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_addStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(GGCodeParser.ADD)
            self.state = 219
            self.shapeStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def squareStatement(self):
            return self.getTypedRuleContext(GGCodeParser.SquareStatementContext,0)


        def rectangleStatement(self):
            return self.getTypedRuleContext(GGCodeParser.RectangleStatementContext,0)


        def circleStatement(self):
            return self.getTypedRuleContext(GGCodeParser.CircleStatementContext,0)


        def lineStatement(self):
            return self.getTypedRuleContext(GGCodeParser.LineStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_shapeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShapeStatement" ):
                listener.enterShapeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShapeStatement" ):
                listener.exitShapeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShapeStatement" ):
                return visitor.visitShapeStatement(self)
            else:
                return visitor.visitChildren(self)




    def shapeStatement(self):

        localctx = GGCodeParser.ShapeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_shapeStatement)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.SQUARE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.squareStatement()
                pass
            elif token in [GGCodeParser.RECTANGLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.rectangleStatement()
                pass
            elif token in [GGCodeParser.CIRCLE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.circleStatement()
                pass
            elif token in [GGCodeParser.LINE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.lineStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SquareStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE(self):
            return self.getToken(GGCodeParser.SQUARE, 0)

        def squareParameters(self):
            return self.getTypedRuleContext(GGCodeParser.SquareParametersContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_squareStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquareStatement" ):
                listener.enterSquareStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquareStatement" ):
                listener.exitSquareStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSquareStatement" ):
                return visitor.visitSquareStatement(self)
            else:
                return visitor.visitChildren(self)




    def squareStatement(self):

        localctx = GGCodeParser.SquareStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_squareStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(GGCodeParser.SQUARE)
            self.state = 228
            self.squareParameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SquareParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def centerClause(self):
            return self.getTypedRuleContext(GGCodeParser.CenterClauseContext,0)


        def lengthClause(self):
            return self.getTypedRuleContext(GGCodeParser.LengthClauseContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_squareParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquareParameters" ):
                listener.enterSquareParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquareParameters" ):
                listener.exitSquareParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSquareParameters" ):
                return visitor.visitSquareParameters(self)
            else:
                return visitor.visitChildren(self)




    def squareParameters(self):

        localctx = GGCodeParser.SquareParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_squareParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.centerClause()
            self.state = 231
            self.lengthClause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RectangleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECTANGLE(self):
            return self.getToken(GGCodeParser.RECTANGLE, 0)

        def centerClause(self):
            return self.getTypedRuleContext(GGCodeParser.CenterClauseContext,0)


        def widthClause(self):
            return self.getTypedRuleContext(GGCodeParser.WidthClauseContext,0)


        def lengthClause(self):
            return self.getTypedRuleContext(GGCodeParser.LengthClauseContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_rectangleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRectangleStatement" ):
                listener.enterRectangleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRectangleStatement" ):
                listener.exitRectangleStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRectangleStatement" ):
                return visitor.visitRectangleStatement(self)
            else:
                return visitor.visitChildren(self)




    def rectangleStatement(self):

        localctx = GGCodeParser.RectangleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_rectangleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(GGCodeParser.RECTANGLE)
            self.state = 234
            self.centerClause()
            self.state = 235
            self.widthClause()
            self.state = 236
            self.lengthClause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CircleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIRCLE(self):
            return self.getToken(GGCodeParser.CIRCLE, 0)

        def centerClause(self):
            return self.getTypedRuleContext(GGCodeParser.CenterClauseContext,0)


        def radiusClause(self):
            return self.getTypedRuleContext(GGCodeParser.RadiusClauseContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_circleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCircleStatement" ):
                listener.enterCircleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCircleStatement" ):
                listener.exitCircleStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCircleStatement" ):
                return visitor.visitCircleStatement(self)
            else:
                return visitor.visitChildren(self)




    def circleStatement(self):

        localctx = GGCodeParser.CircleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_circleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(GGCodeParser.CIRCLE)
            self.state = 239
            self.centerClause()
            self.state = 240
            self.radiusClause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE(self):
            return self.getToken(GGCodeParser.LINE, 0)

        def fromClause(self):
            return self.getTypedRuleContext(GGCodeParser.FromClauseContext,0)


        def toClause(self):
            return self.getTypedRuleContext(GGCodeParser.ToClauseContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_lineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineStatement" ):
                listener.enterLineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineStatement" ):
                listener.exitLineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineStatement" ):
                return visitor.visitLineStatement(self)
            else:
                return visitor.visitChildren(self)




    def lineStatement(self):

        localctx = GGCodeParser.LineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(GGCodeParser.LINE)
            self.state = 243
            self.fromClause()
            self.state = 244
            self.toClause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CenterClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CENTER(self):
            return self.getToken(GGCodeParser.CENTER, 0)

        def coordinatePair(self):
            return self.getTypedRuleContext(GGCodeParser.CoordinatePairContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_centerClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCenterClause" ):
                listener.enterCenterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCenterClause" ):
                listener.exitCenterClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCenterClause" ):
                return visitor.visitCenterClause(self)
            else:
                return visitor.visitChildren(self)




    def centerClause(self):

        localctx = GGCodeParser.CenterClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_centerClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(GGCodeParser.CENTER)
            self.state = 247
            self.coordinatePair()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WIDTH(self):
            return self.getToken(GGCodeParser.WIDTH, 0)

        def numericValue(self):
            return self.getTypedRuleContext(GGCodeParser.NumericValueContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_widthClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidthClause" ):
                listener.enterWidthClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidthClause" ):
                listener.exitWidthClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWidthClause" ):
                return visitor.visitWidthClause(self)
            else:
                return visitor.visitChildren(self)




    def widthClause(self):

        localctx = GGCodeParser.WidthClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_widthClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GGCodeParser.WIDTH)
            self.state = 250
            self.numericValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LengthClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LENGTH(self):
            return self.getToken(GGCodeParser.LENGTH, 0)

        def numericValue(self):
            return self.getTypedRuleContext(GGCodeParser.NumericValueContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_lengthClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLengthClause" ):
                listener.enterLengthClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLengthClause" ):
                listener.exitLengthClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLengthClause" ):
                return visitor.visitLengthClause(self)
            else:
                return visitor.visitChildren(self)




    def lengthClause(self):

        localctx = GGCodeParser.LengthClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_lengthClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(GGCodeParser.LENGTH)
            self.state = 253
            self.numericValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RadiusClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RADIUS(self):
            return self.getToken(GGCodeParser.RADIUS, 0)

        def numericValue(self):
            return self.getTypedRuleContext(GGCodeParser.NumericValueContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_radiusClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRadiusClause" ):
                listener.enterRadiusClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRadiusClause" ):
                listener.exitRadiusClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRadiusClause" ):
                return visitor.visitRadiusClause(self)
            else:
                return visitor.visitChildren(self)




    def radiusClause(self):

        localctx = GGCodeParser.RadiusClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_radiusClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(GGCodeParser.RADIUS)
            self.state = 256
            self.numericValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(GGCodeParser.FROM, 0)

        def coordinatePair(self):
            return self.getTypedRuleContext(GGCodeParser.CoordinatePairContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_fromClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromClause" ):
                listener.enterFromClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromClause" ):
                listener.exitFromClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromClause" ):
                return visitor.visitFromClause(self)
            else:
                return visitor.visitChildren(self)




    def fromClause(self):

        localctx = GGCodeParser.FromClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_fromClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(GGCodeParser.FROM)
            self.state = 259
            self.coordinatePair()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TO(self):
            return self.getToken(GGCodeParser.TO, 0)

        def coordinatePair(self):
            return self.getTypedRuleContext(GGCodeParser.CoordinatePairContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_toClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToClause" ):
                listener.enterToClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToClause" ):
                listener.exitToClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToClause" ):
                return visitor.visitToClause(self)
            else:
                return visitor.visitChildren(self)




    def toClause(self):

        localctx = GGCodeParser.ToClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_toClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(GGCodeParser.TO)
            self.state = 262
            self.coordinatePair()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordinatePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.NumericValueContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.NumericValueContext,i)


        def getRuleIndex(self):
            return GGCodeParser.RULE_coordinatePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordinatePair" ):
                listener.enterCoordinatePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordinatePair" ):
                listener.exitCoordinatePair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoordinatePair" ):
                return visitor.visitCoordinatePair(self)
            else:
                return visitor.visitChildren(self)




    def coordinatePair(self):

        localctx = GGCodeParser.CoordinatePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_coordinatePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.numericValue()
            self.state = 265
            self.numericValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinitionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defineStatement(self):
            return self.getTypedRuleContext(GGCodeParser.DefineStatementContext,0)


        def setStatement(self):
            return self.getTypedRuleContext(GGCodeParser.SetStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_definitionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinitionStatement" ):
                listener.enterDefinitionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinitionStatement" ):
                listener.exitDefinitionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinitionStatement" ):
                return visitor.visitDefinitionStatement(self)
            else:
                return visitor.visitChildren(self)




    def definitionStatement(self):

        localctx = GGCodeParser.DefinitionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_definitionStatement)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.DEFINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.defineStatement()
                pass
            elif token in [GGCodeParser.SET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.setStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefineStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(GGCodeParser.DEFINE, 0)

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def AS(self):
            return self.getToken(GGCodeParser.AS, 0)

        def locationDefinition(self):
            return self.getTypedRuleContext(GGCodeParser.LocationDefinitionContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_defineStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineStatement" ):
                listener.enterDefineStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineStatement" ):
                listener.exitDefineStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineStatement" ):
                return visitor.visitDefineStatement(self)
            else:
                return visitor.visitChildren(self)




    def defineStatement(self):

        localctx = GGCodeParser.DefineStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_defineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(GGCodeParser.DEFINE)
            self.state = 272
            self.match(GGCodeParser.IDENTIFIER)
            self.state = 273
            self.match(GGCodeParser.AS)
            self.state = 274
            self.locationDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coordinatePair(self):
            return self.getTypedRuleContext(GGCodeParser.CoordinatePairContext,0)


        def pointTarget(self):
            return self.getTypedRuleContext(GGCodeParser.PointTargetContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_locationDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocationDefinition" ):
                listener.enterLocationDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocationDefinition" ):
                listener.exitLocationDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocationDefinition" ):
                return visitor.visitLocationDefinition(self)
            else:
                return visitor.visitChildren(self)




    def locationDefinition(self):

        localctx = GGCodeParser.LocationDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_locationDefinition)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.INTERGER, GGCodeParser.DECIMAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.coordinatePair()
                pass
            elif token in [GGCodeParser.BASE, GGCodeParser.CENTER_POINT, GGCodeParser.ORIGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.pointTarget()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(GGCodeParser.SET, 0)

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def TO(self):
            return self.getToken(GGCodeParser.TO, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_setStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStatement" ):
                listener.enterSetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStatement" ):
                listener.exitSetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStatement" ):
                return visitor.visitSetStatement(self)
            else:
                return visitor.visitChildren(self)




    def setStatement(self):

        localctx = GGCodeParser.SetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(GGCodeParser.SET)
            self.state = 281
            self.match(GGCodeParser.IDENTIFIER)
            self.state = 282
            self.match(GGCodeParser.TO)
            self.state = 283
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GGCodeParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(GGCodeParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(GGCodeParser.THEN, 0)

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.BlockStatementContext,i)


        def ELSE(self):
            return self.getToken(GGCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalStatement" ):
                return visitor.visitConditionalStatement(self)
            else:
                return visitor.visitChildren(self)




    def conditionalStatement(self):

        localctx = GGCodeParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(GGCodeParser.IF)
            self.state = 286
            self.condition()
            self.state = 287
            self.match(GGCodeParser.THEN)
            self.state = 288
            self.blockStatement()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GGCodeParser.ELSE:
                self.state = 289
                self.match(GGCodeParser.ELSE)
                self.state = 290
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(GGCodeParser.REPEAT, 0)

        def repeatCount(self):
            return self.getTypedRuleContext(GGCodeParser.RepeatCountContext,0)


        def TIMES(self):
            return self.getToken(GGCodeParser.TIMES, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(GGCodeParser.BlockStatementContext,0)


        def WHILE(self):
            return self.getToken(GGCodeParser.WHILE, 0)

        def condition(self):
            return self.getTypedRuleContext(GGCodeParser.ConditionContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = GGCodeParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_loopStatement)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.REPEAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(GGCodeParser.REPEAT)
                self.state = 294
                self.repeatCount()
                self.state = 295
                self.match(GGCodeParser.TIMES)
                self.state = 296
                self.blockStatement()
                pass
            elif token in [GGCodeParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(GGCodeParser.WHILE)
                self.state = 299
                self.condition()
                self.state = 300
                self.blockStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatCountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERGER(self):
            return self.getToken(GGCodeParser.INTERGER, 0)

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_repeatCount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatCount" ):
                listener.enterRepeatCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatCount" ):
                listener.exitRepeatCount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatCount" ):
                return visitor.visitRepeatCount(self)
            else:
                return visitor.visitChildren(self)




    def repeatCount(self):

        localctx = GGCodeParser.RepeatCountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_repeatCount)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            _la = self._input.LA(1)
            if not(_la==GGCodeParser.IDENTIFIER or _la==GGCodeParser.INTERGER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(GGCodeParser.LBRACE, 0)

        def statementList(self):
            return self.getTypedRuleContext(GGCodeParser.StatementListContext,0)


        def RBRACE(self):
            return self.getToken(GGCodeParser.RBRACE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = GGCodeParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(GGCodeParser.LBRACE)
            self.state = 307
            self.statementList()
            self.state = 308
            self.match(GGCodeParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = GGCodeParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonExpression(self):
            return self.getTypedRuleContext(GGCodeParser.ComparisonExpressionContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = GGCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.comparisonExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(GGCodeParser.AdditiveExpressionContext,0)


        def comparisonTail(self):
            return self.getTypedRuleContext(GGCodeParser.ComparisonTailContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_comparisonExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpression" ):
                listener.enterComparisonExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpression" ):
                listener.exitComparisonExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpression" ):
                return visitor.visitComparisonExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpression(self):

        localctx = GGCodeParser.ComparisonExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_comparisonExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.additiveExpression()
            self.state = 315
            self.comparisonTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonOperator(self):
            return self.getTypedRuleContext(GGCodeParser.ComparisonOperatorContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(GGCodeParser.AdditiveExpressionContext,0)


        def comparisonTail(self):
            return self.getTypedRuleContext(GGCodeParser.ComparisonTailContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_comparisonTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonTail" ):
                listener.enterComparisonTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonTail" ):
                listener.exitComparisonTail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonTail" ):
                return visitor.visitComparisonTail(self)
            else:
                return visitor.visitChildren(self)




    def comparisonTail(self):

        localctx = GGCodeParser.ComparisonTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_comparisonTail)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.EQ, GGCodeParser.NEQ, GGCodeParser.GT, GGCodeParser.LT, GGCodeParser.GTE, GGCodeParser.LTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.comparisonOperator()
                self.state = 318
                self.additiveExpression()
                self.state = 319
                self.comparisonTail()
                pass
            elif token in [GGCodeParser.EOF, GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.THEN, GGCodeParser.WHILE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.RPAREN, GGCodeParser.LBRACE, GGCodeParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(GGCodeParser.MultiplicativeExpressionContext,0)


        def additiveTail(self):
            return self.getTypedRuleContext(GGCodeParser.AdditiveTailContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = GGCodeParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_additiveExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.multiplicativeExpression()
            self.state = 325
            self.additiveTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addOperator(self):
            return self.getTypedRuleContext(GGCodeParser.AddOperatorContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(GGCodeParser.MultiplicativeExpressionContext,0)


        def additiveTail(self):
            return self.getTypedRuleContext(GGCodeParser.AdditiveTailContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_additiveTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveTail" ):
                listener.enterAdditiveTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveTail" ):
                listener.exitAdditiveTail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveTail" ):
                return visitor.visitAdditiveTail(self)
            else:
                return visitor.visitChildren(self)




    def additiveTail(self):

        localctx = GGCodeParser.AdditiveTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_additiveTail)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.PLUS, GGCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.addOperator()
                self.state = 328
                self.multiplicativeExpression()
                self.state = 329
                self.additiveTail()
                pass
            elif token in [GGCodeParser.EOF, GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.THEN, GGCodeParser.WHILE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.RPAREN, GGCodeParser.LBRACE, GGCodeParser.RBRACE, GGCodeParser.EQ, GGCodeParser.NEQ, GGCodeParser.GT, GGCodeParser.LT, GGCodeParser.GTE, GGCodeParser.LTE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(GGCodeParser.UnaryExpressionContext,0)


        def multiplicativeTail(self):
            return self.getTypedRuleContext(GGCodeParser.MultiplicativeTailContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = GGCodeParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_multiplicativeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.unaryExpression()
            self.state = 335
            self.multiplicativeTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulOperator(self):
            return self.getTypedRuleContext(GGCodeParser.MulOperatorContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(GGCodeParser.UnaryExpressionContext,0)


        def multiplicativeTail(self):
            return self.getTypedRuleContext(GGCodeParser.MultiplicativeTailContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_multiplicativeTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeTail" ):
                listener.enterMultiplicativeTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeTail" ):
                listener.exitMultiplicativeTail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeTail" ):
                return visitor.visitMultiplicativeTail(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeTail(self):

        localctx = GGCodeParser.MultiplicativeTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_multiplicativeTail)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.STAR, GGCodeParser.SLASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.mulOperator()
                self.state = 338
                self.unaryExpression()
                self.state = 339
                self.multiplicativeTail()
                pass
            elif token in [GGCodeParser.EOF, GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.THEN, GGCodeParser.WHILE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.RPAREN, GGCodeParser.LBRACE, GGCodeParser.RBRACE, GGCodeParser.PLUS, GGCodeParser.MINUS, GGCodeParser.EQ, GGCodeParser.NEQ, GGCodeParser.GT, GGCodeParser.LT, GGCodeParser.GTE, GGCodeParser.LTE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(GGCodeParser.MINUS, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(GGCodeParser.UnaryExpressionContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(GGCodeParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = GGCodeParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_unaryExpression)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(GGCodeParser.MINUS)
                self.state = 345
                self.unaryExpression()
                pass
            elif token in [GGCodeParser.LPAREN, GGCodeParser.IDENTIFIER, GGCodeParser.INTERGER, GGCodeParser.DECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericValue(self):
            return self.getTypedRuleContext(GGCodeParser.NumericValueContext,0)


        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(GGCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GGCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = GGCodeParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_primaryExpression)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.INTERGER, GGCodeParser.DECIMAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.numericValue()
                pass
            elif token in [GGCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(GGCodeParser.IDENTIFIER)
                pass
            elif token in [GGCodeParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 351
                self.match(GGCodeParser.LPAREN)
                self.state = 352
                self.expression()
                self.state = 353
                self.match(GGCodeParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(GGCodeParser.EQ, 0)

        def NEQ(self):
            return self.getToken(GGCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(GGCodeParser.LT, 0)

        def LTE(self):
            return self.getToken(GGCodeParser.LTE, 0)

        def GT(self):
            return self.getToken(GGCodeParser.GT, 0)

        def GTE(self):
            return self.getToken(GGCodeParser.GTE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = GGCodeParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.EQ) | (1 << GGCodeParser.NEQ) | (1 << GGCodeParser.GT) | (1 << GGCodeParser.LT) | (1 << GGCodeParser.GTE) | (1 << GGCodeParser.LTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(GGCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GGCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_addOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOperator" ):
                listener.enterAddOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOperator" ):
                listener.exitAddOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOperator" ):
                return visitor.visitAddOperator(self)
            else:
                return visitor.visitChildren(self)




    def addOperator(self):

        localctx = GGCodeParser.AddOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_addOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==GGCodeParser.PLUS or _la==GGCodeParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(GGCodeParser.STAR, 0)

        def SLASH(self):
            return self.getToken(GGCodeParser.SLASH, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_mulOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulOperator" ):
                listener.enterMulOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulOperator" ):
                listener.exitMulOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOperator" ):
                return visitor.visitMulOperator(self)
            else:
                return visitor.visitChildren(self)




    def mulOperator(self):

        localctx = GGCodeParser.MulOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_mulOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            _la = self._input.LA(1)
            if not(_la==GGCodeParser.STAR or _la==GGCodeParser.SLASH):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERGER(self):
            return self.getToken(GGCodeParser.INTERGER, 0)

        def DECIMAL(self):
            return self.getToken(GGCodeParser.DECIMAL, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_numericValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericValue" ):
                listener.enterNumericValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericValue" ):
                listener.exitNumericValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericValue" ):
                return visitor.visitNumericValue(self)
            else:
                return visitor.visitChildren(self)




    def numericValue(self):

        localctx = GGCodeParser.NumericValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_numericValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            _la = self._input.LA(1)
            if not(_la==GGCodeParser.INTERGER or _la==GGCodeParser.DECIMAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MeasureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEASURE(self):
            return self.getToken(GGCodeParser.MEASURE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_measure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeasure" ):
                listener.enterMeasure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeasure" ):
                listener.exitMeasure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeasure" ):
                return visitor.visitMeasure(self)
            else:
                return visitor.visitChildren(self)




    def measure(self):

        localctx = GGCodeParser.MeasureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_measure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(GGCodeParser.MEASURE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





