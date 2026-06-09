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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u019a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0090\n\3\3\4\3\4\5")
        buf.write("\4\u0094\n\4\3\5\3\5\3\5\3\5\5\5\u009a\n\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u00a0\n\6\3\7\3\7\3\7\3\7\5\7\u00a6\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\5\t\u00ae\n\t\3\n\3\n\7\n\u00b2\n\n")
        buf.write("\f\n\16\n\u00b5\13\n\3\13\3\13\3\f\3\f\3\f\5\f\u00bc\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\5\r\u00c3\n\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\5\26\u00e0\n\26\3\27\3\27\3\27\3\27\5\27\u00e6")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u00ef\n")
        buf.write("\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u00ff\n\35\3\36\3\36\3\37\3")
        buf.write("\37\3 \3 \3 \3!\3!\3!\3!\5!\u010c\n!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-")
        buf.write("\3-\3.\3.\5.\u0138\n.\3/\3/\3/\3/\3/\3\60\3\60\5\60\u0141")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\5\62\u014e\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u0159\n\63\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\39\39\59\u016d")
        buf.write("\n9\3:\3:\3:\3;\3;\3;\3;\3;\5;\u0177\n;\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\5=\u0181\n=\3>\3>\3>\5>\u0186\n>\3?\3?\3?\3")
        buf.write("?\3?\3?\5?\u018e\n?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3D\2")
        buf.write("\2E\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\2\t\3\2\3\6\3\2\31\33\3\2@A\3\2\67<\3\2\63")
        buf.write("\64\3\2\65\66\3\2AB\2\u017b\2\u0088\3\2\2\2\4\u008f\3")
        buf.write("\2\2\2\6\u0093\3\2\2\2\b\u0099\3\2\2\2\n\u009f\3\2\2\2")
        buf.write("\f\u00a5\3\2\2\2\16\u00a7\3\2\2\2\20\u00ab\3\2\2\2\22")
        buf.write("\u00af\3\2\2\2\24\u00b6\3\2\2\2\26\u00bb\3\2\2\2\30\u00c2")
        buf.write("\3\2\2\2\32\u00c4\3\2\2\2\34\u00c6\3\2\2\2\36\u00c9\3")
        buf.write("\2\2\2 \u00cd\3\2\2\2\"\u00d0\3\2\2\2$\u00d4\3\2\2\2&")
        buf.write("\u00d6\3\2\2\2(\u00d8\3\2\2\2*\u00dc\3\2\2\2,\u00e5\3")
        buf.write("\2\2\2.\u00e7\3\2\2\2\60\u00ee\3\2\2\2\62\u00f0\3\2\2")
        buf.write("\2\64\u00f3\3\2\2\2\66\u00f7\3\2\2\28\u00fe\3\2\2\2:\u0100")
        buf.write("\3\2\2\2<\u0102\3\2\2\2>\u0104\3\2\2\2@\u010b\3\2\2\2")
        buf.write("B\u010d\3\2\2\2D\u0110\3\2\2\2F\u0113\3\2\2\2H\u0118\3")
        buf.write("\2\2\2J\u011c\3\2\2\2L\u0120\3\2\2\2N\u0123\3\2\2\2P\u0126")
        buf.write("\3\2\2\2R\u0129\3\2\2\2T\u012c\3\2\2\2V\u012f\3\2\2\2")
        buf.write("X\u0132\3\2\2\2Z\u0137\3\2\2\2\\\u0139\3\2\2\2^\u0140")
        buf.write("\3\2\2\2`\u0142\3\2\2\2b\u0147\3\2\2\2d\u0158\3\2\2\2")
        buf.write("f\u015a\3\2\2\2h\u015c\3\2\2\2j\u0160\3\2\2\2l\u0162\3")
        buf.write("\2\2\2n\u0164\3\2\2\2p\u016c\3\2\2\2r\u016e\3\2\2\2t\u0176")
        buf.write("\3\2\2\2v\u0178\3\2\2\2x\u0180\3\2\2\2z\u0185\3\2\2\2")
        buf.write("|\u018d\3\2\2\2~\u018f\3\2\2\2\u0080\u0191\3\2\2\2\u0082")
        buf.write("\u0193\3\2\2\2\u0084\u0195\3\2\2\2\u0086\u0197\3\2\2\2")
        buf.write("\u0088\u0089\5\4\3\2\u0089\u008a\7\2\2\3\u008a\3\3\2\2")
        buf.write("\2\u008b\u008c\5\6\4\2\u008c\u008d\5\4\3\2\u008d\u0090")
        buf.write("\3\2\2\2\u008e\u0090\5\6\4\2\u008f\u008b\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\5\3\2\2\2\u0091\u0094\5\b\5\2\u0092")
        buf.write("\u0094\5\n\6\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\7\3\2\2\2\u0095\u009a\5\f\7\2\u0096\u009a\5\60")
        buf.write("\31\2\u0097\u009a\5<\37\2\u0098\u009a\5Z.\2\u0099\u0095")
        buf.write("\3\2\2\2\u0099\u0096\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\t\3\2\2\2\u009b\u00a0\5b\62\2\u009c")
        buf.write("\u00a0\5d\63\2\u009d\u00a0\5h\65\2\u009e\u00a0\5.\30\2")
        buf.write("\u009f\u009b\3\2\2\2\u009f\u009c\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u009f\u009e\3\2\2\2\u00a0\13\3\2\2\2\u00a1\u00a6")
        buf.write("\5\16\b\2\u00a2\u00a6\5(\25\2\u00a3\u00a6\5*\26\2\u00a4")
        buf.write("\u00a6\5\20\t\2\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2")
        buf.write("\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\r\3\2")
        buf.write("\2\2\u00a7\u00a8\7\r\2\2\u00a8\u00a9\7\16\2\2\u00a9\u00aa")
        buf.write("\5\26\f\2\u00aa\17\3\2\2\2\u00ab\u00ad\7*\2\2\u00ac\u00ae")
        buf.write("\5\22\n\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\21\3\2\2\2\u00af\u00b3\5\24\13\2\u00b0\u00b2\5\24\13")
        buf.write("\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\23\3\2\2\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b6\u00b7\t\2\2\2\u00b7\25\3\2\2\2\u00b8\u00bc")
        buf.write("\5\30\r\2\u00b9\u00bc\5$\23\2\u00ba\u00bc\5&\24\2\u00bb")
        buf.write("\u00b8\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc\27\3\2\2\2\u00bd\u00c3\5\32\16\2\u00be\u00c3\5")
        buf.write("\34\17\2\u00bf\u00c3\5\36\20\2\u00c0\u00c3\5 \21\2\u00c1")
        buf.write("\u00c3\5\"\22\2\u00c2\u00bd\3\2\2\2\u00c2\u00be\3\2\2")
        buf.write("\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\31\3\2\2\2\u00c4\u00c5\7?\2\2\u00c5\33")
        buf.write("\3\2\2\2\u00c6\u00c7\7?\2\2\u00c7\u00c8\7?\2\2\u00c8\35")
        buf.write("\3\2\2\2\u00c9\u00ca\7?\2\2\u00ca\u00cb\7?\2\2\u00cb\u00cc")
        buf.write("\7?\2\2\u00cc\37\3\2\2\2\u00cd\u00ce\5\u0086D\2\u00ce")
        buf.write("\u00cf\5\u0086D\2\u00cf!\3\2\2\2\u00d0\u00d1\5\u0086D")
        buf.write("\2\u00d1\u00d2\5\u0086D\2\u00d2\u00d3\5\u0086D\2\u00d3")
        buf.write("#\3\2\2\2\u00d4\u00d5\t\3\2\2\u00d5%\3\2\2\2\u00d6\u00d7")
        buf.write("\7@\2\2\u00d7\'\3\2\2\2\u00d8\u00d9\7\7\2\2\u00d9\u00da")
        buf.write("\7\t\2\2\u00da\u00db\5\u0086D\2\u00db)\3\2\2\2\u00dc\u00df")
        buf.write("\7\b\2\2\u00dd\u00de\7\t\2\2\u00de\u00e0\5,\27\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0+\3\2\2\2\u00e1")
        buf.write("\u00e2\7\n\2\2\u00e2\u00e6\7A\2\2\u00e3\u00e4\7\13\2\2")
        buf.write("\u00e4\u00e6\5\u0086D\2\u00e5\u00e1\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e6-\3\2\2\2\u00e7\u00e8\7\t\2\2\u00e8\u00e9")
        buf.write("\5,\27\2\u00e9\u00ea\5h\65\2\u00ea/\3\2\2\2\u00eb\u00ef")
        buf.write("\5\62\32\2\u00ec\u00ef\5\64\33\2\u00ed\u00ef\5\66\34\2")
        buf.write("\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ef\61\3\2\2\2\u00f0\u00f1\7\f\2\2\u00f1\u00f2")
        buf.write("\5:\36\2\u00f2\63\3\2\2\2\u00f3\u00f4\7%\2\2\u00f4\u00f5")
        buf.write("\7&\2\2\u00f5\u00f6\58\35\2\u00f6\65\3\2\2\2\u00f7\u00f8")
        buf.write("\7)\2\2\u00f8\u00f9\7@\2\2\u00f9\67\3\2\2\2\u00fa\u00fb")
        buf.write("\7A\2\2\u00fb\u00ff\7\'\2\2\u00fc\u00fd\7A\2\2\u00fd\u00ff")
        buf.write("\7(\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write("9\3\2\2\2\u0100\u0101\7>\2\2\u0101;\3\2\2\2\u0102\u0103")
        buf.write("\5> \2\u0103=\3\2\2\2\u0104\u0105\7\17\2\2\u0105\u0106")
        buf.write("\5@!\2\u0106?\3\2\2\2\u0107\u010c\5B\"\2\u0108\u010c\5")
        buf.write("F$\2\u0109\u010c\5H%\2\u010a\u010c\5J&\2\u010b\u0107\3")
        buf.write("\2\2\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a")
        buf.write("\3\2\2\2\u010cA\3\2\2\2\u010d\u010e\7\20\2\2\u010e\u010f")
        buf.write("\5D#\2\u010fC\3\2\2\2\u0110\u0111\5L\'\2\u0111\u0112\5")
        buf.write("P)\2\u0112E\3\2\2\2\u0113\u0114\7\24\2\2\u0114\u0115\5")
        buf.write("L\'\2\u0115\u0116\5N(\2\u0116\u0117\5P)\2\u0117G\3\2\2")
        buf.write("\2\u0118\u0119\7\25\2\2\u0119\u011a\5L\'\2\u011a\u011b")
        buf.write("\5R*\2\u011bI\3\2\2\2\u011c\u011d\7\27\2\2\u011d\u011e")
        buf.write("\5T+\2\u011e\u011f\5V,\2\u011fK\3\2\2\2\u0120\u0121\7")
        buf.write("\21\2\2\u0121\u0122\5X-\2\u0122M\3\2\2\2\u0123\u0124\7")
        buf.write("\23\2\2\u0124\u0125\5\u0084C\2\u0125O\3\2\2\2\u0126\u0127")
        buf.write("\7\22\2\2\u0127\u0128\5\u0084C\2\u0128Q\3\2\2\2\u0129")
        buf.write("\u012a\7\26\2\2\u012a\u012b\5\u0084C\2\u012bS\3\2\2\2")
        buf.write("\u012c\u012d\7\30\2\2\u012d\u012e\5X-\2\u012eU\3\2\2\2")
        buf.write("\u012f\u0130\7\16\2\2\u0130\u0131\5X-\2\u0131W\3\2\2\2")
        buf.write("\u0132\u0133\5\u0084C\2\u0133\u0134\5\u0084C\2\u0134Y")
        buf.write("\3\2\2\2\u0135\u0138\5\\/\2\u0136\u0138\5`\61\2\u0137")
        buf.write("\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138[\3\2\2\2\u0139")
        buf.write("\u013a\7\35\2\2\u013a\u013b\7@\2\2\u013b\u013c\7\36\2")
        buf.write("\2\u013c\u013d\5^\60\2\u013d]\3\2\2\2\u013e\u0141\5X-")
        buf.write("\2\u013f\u0141\5$\23\2\u0140\u013e\3\2\2\2\u0140\u013f")
        buf.write("\3\2\2\2\u0141_\3\2\2\2\u0142\u0143\7\34\2\2\u0143\u0144")
        buf.write("\7@\2\2\u0144\u0145\7\16\2\2\u0145\u0146\5l\67\2\u0146")
        buf.write("a\3\2\2\2\u0147\u0148\7!\2\2\u0148\u0149\5j\66\2\u0149")
        buf.write("\u014a\7\"\2\2\u014a\u014d\5h\65\2\u014b\u014c\7#\2\2")
        buf.write("\u014c\u014e\5h\65\2\u014d\u014b\3\2\2\2\u014d\u014e\3")
        buf.write("\2\2\2\u014ec\3\2\2\2\u014f\u0150\7\37\2\2\u0150\u0151")
        buf.write("\5f\64\2\u0151\u0152\7 \2\2\u0152\u0153\5h\65\2\u0153")
        buf.write("\u0159\3\2\2\2\u0154\u0155\7$\2\2\u0155\u0156\5j\66\2")
        buf.write("\u0156\u0157\5h\65\2\u0157\u0159\3\2\2\2\u0158\u014f\3")
        buf.write("\2\2\2\u0158\u0154\3\2\2\2\u0159e\3\2\2\2\u015a\u015b")
        buf.write("\t\4\2\2\u015bg\3\2\2\2\u015c\u015d\7\61\2\2\u015d\u015e")
        buf.write("\5\4\3\2\u015e\u015f\7\62\2\2\u015fi\3\2\2\2\u0160\u0161")
        buf.write("\5l\67\2\u0161k\3\2\2\2\u0162\u0163\5n8\2\u0163m\3\2\2")
        buf.write("\2\u0164\u0165\5r:\2\u0165\u0166\5p9\2\u0166o\3\2\2\2")
        buf.write("\u0167\u0168\5~@\2\u0168\u0169\5r:\2\u0169\u016a\5p9\2")
        buf.write("\u016a\u016d\3\2\2\2\u016b\u016d\3\2\2\2\u016c\u0167\3")
        buf.write("\2\2\2\u016c\u016b\3\2\2\2\u016dq\3\2\2\2\u016e\u016f")
        buf.write("\5v<\2\u016f\u0170\5t;\2\u0170s\3\2\2\2\u0171\u0172\5")
        buf.write("\u0080A\2\u0172\u0173\5v<\2\u0173\u0174\5t;\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0171\3\2\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177u\3\2\2\2\u0178\u0179\5z>\2\u0179")
        buf.write("\u017a\5x=\2\u017aw\3\2\2\2\u017b\u017c\5\u0082B\2\u017c")
        buf.write("\u017d\5z>\2\u017d\u017e\5x=\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u017b\3\2\2\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181y\3\2\2\2\u0182\u0183\7\64\2\2\u0183\u0186\5z>\2")
        buf.write("\u0184\u0186\5|?\2\u0185\u0182\3\2\2\2\u0185\u0184\3\2")
        buf.write("\2\2\u0186{\3\2\2\2\u0187\u018e\5\u0084C\2\u0188\u018e")
        buf.write("\7@\2\2\u0189\u018a\7/\2\2\u018a\u018b\5l\67\2\u018b\u018c")
        buf.write("\7\60\2\2\u018c\u018e\3\2\2\2\u018d\u0187\3\2\2\2\u018d")
        buf.write("\u0188\3\2\2\2\u018d\u0189\3\2\2\2\u018e}\3\2\2\2\u018f")
        buf.write("\u0190\t\5\2\2\u0190\177\3\2\2\2\u0191\u0192\t\6\2\2\u0192")
        buf.write("\u0081\3\2\2\2\u0193\u0194\t\7\2\2\u0194\u0083\3\2\2\2")
        buf.write("\u0195\u0196\t\b\2\2\u0196\u0085\3\2\2\2\u0197\u0198\7")
        buf.write("=\2\2\u0198\u0087\3\2\2\2\31\u008f\u0093\u0099\u009f\u00a5")
        buf.write("\u00ad\u00b3\u00bb\u00c2\u00df\u00e5\u00ee\u00fe\u010b")
        buf.write("\u0137\u0140\u014d\u0158\u016c\u0176\u0180\u0185\u018d")
        return buf.getvalue()


class GGCodeParser ( Parser ):

    grammarFileName = "GGCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'X'", "'Y'", "'Z'", "'E'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STOP", "PAUSE", "AT", "LAYER", "HEIGHT", 
                      "TEMPERATURE", "MOVE", "TO", "ADD", "SQUARE", "CENTER", 
                      "LENGTH", "WIDTH", "RECTANGLE", "CIRCLE", "RADIUS", 
                      "LINE", "FROM", "BASE", "CENTER_POINT", "ORIGIN", 
                      "SET", "DEFINE", "AS", "REPEAT", "TIMES", "IF", "THEN", 
                      "ELSE", "WHILE", "WAIT", "FOR", "SECONDS", "MINUTES", 
                      "USE", "HOME", "KEY_X", "KEY_Y", "KEY_Z", "KEY_E", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", 
                      "STAR", "SLASH", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", 
                      "MEASURE", "TEMPERATURE_VALUE", "AXIS_VALUE", "IDENTIFIER", 
                      "INTERGER", "DECIMAL", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "GCODE_COMMENT" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_simpleStatement = 3
    RULE_compoundStatement = 4
    RULE_motionStatement = 5
    RULE_moveStatement = 6
    RULE_homeStatement = 7
    RULE_axisList = 8
    RULE_axis = 9
    RULE_moveTarget = 10
    RULE_coordinateTarget = 11
    RULE_axisSingle = 12
    RULE_axisPair = 13
    RULE_axisTriplet = 14
    RULE_measurePair = 15
    RULE_measureTriplet = 16
    RULE_pointTarget = 17
    RULE_namedTarget = 18
    RULE_stopStatement = 19
    RULE_pauseStatement = 20
    RULE_anchorTarget = 21
    RULE_atBlockStatement = 22
    RULE_machineStatement = 23
    RULE_temperatureStatement = 24
    RULE_waitStatement = 25
    RULE_useStatement = 26
    RULE_durationValue = 27
    RULE_temperatureValue = 28
    RULE_geometryStatement = 29
    RULE_addStatement = 30
    RULE_shapeStatement = 31
    RULE_squareStatement = 32
    RULE_squareParameters = 33
    RULE_rectangleStatement = 34
    RULE_circleStatement = 35
    RULE_lineStatement = 36
    RULE_centerClause = 37
    RULE_widthClause = 38
    RULE_lengthClause = 39
    RULE_radiusClause = 40
    RULE_fromClause = 41
    RULE_toClause = 42
    RULE_coordinatePair = 43
    RULE_definitionStatement = 44
    RULE_defineStatement = 45
    RULE_locationDefinition = 46
    RULE_setStatement = 47
    RULE_conditionalStatement = 48
    RULE_loopStatement = 49
    RULE_repeatCount = 50
    RULE_blockStatement = 51
    RULE_condition = 52
    RULE_expression = 53
    RULE_comparisonExpression = 54
    RULE_comparisonTail = 55
    RULE_additiveExpression = 56
    RULE_additiveTail = 57
    RULE_multiplicativeExpression = 58
    RULE_multiplicativeTail = 59
    RULE_unaryExpression = 60
    RULE_primaryExpression = 61
    RULE_comparisonOperator = 62
    RULE_addOperator = 63
    RULE_mulOperator = 64
    RULE_numericValue = 65
    RULE_measure = 66

    ruleNames =  [ "program", "statementList", "statement", "simpleStatement", 
                   "compoundStatement", "motionStatement", "moveStatement", 
                   "homeStatement", "axisList", "axis", "moveTarget", "coordinateTarget", 
                   "axisSingle", "axisPair", "axisTriplet", "measurePair", 
                   "measureTriplet", "pointTarget", "namedTarget", "stopStatement", 
                   "pauseStatement", "anchorTarget", "atBlockStatement", 
                   "machineStatement", "temperatureStatement", "waitStatement", 
                   "useStatement", "durationValue", "temperatureValue", 
                   "geometryStatement", "addStatement", "shapeStatement", 
                   "squareStatement", "squareParameters", "rectangleStatement", 
                   "circleStatement", "lineStatement", "centerClause", "widthClause", 
                   "lengthClause", "radiusClause", "fromClause", "toClause", 
                   "coordinatePair", "definitionStatement", "defineStatement", 
                   "locationDefinition", "setStatement", "conditionalStatement", 
                   "loopStatement", "repeatCount", "blockStatement", "condition", 
                   "expression", "comparisonExpression", "comparisonTail", 
                   "additiveExpression", "additiveTail", "multiplicativeExpression", 
                   "multiplicativeTail", "unaryExpression", "primaryExpression", 
                   "comparisonOperator", "addOperator", "mulOperator", "numericValue", 
                   "measure" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    STOP=5
    PAUSE=6
    AT=7
    LAYER=8
    HEIGHT=9
    TEMPERATURE=10
    MOVE=11
    TO=12
    ADD=13
    SQUARE=14
    CENTER=15
    LENGTH=16
    WIDTH=17
    RECTANGLE=18
    CIRCLE=19
    RADIUS=20
    LINE=21
    FROM=22
    BASE=23
    CENTER_POINT=24
    ORIGIN=25
    SET=26
    DEFINE=27
    AS=28
    REPEAT=29
    TIMES=30
    IF=31
    THEN=32
    ELSE=33
    WHILE=34
    WAIT=35
    FOR=36
    SECONDS=37
    MINUTES=38
    USE=39
    HOME=40
    KEY_X=41
    KEY_Y=42
    KEY_Z=43
    KEY_E=44
    LPAREN=45
    RPAREN=46
    LBRACE=47
    RBRACE=48
    PLUS=49
    MINUS=50
    STAR=51
    SLASH=52
    EQ=53
    NEQ=54
    GT=55
    LT=56
    GTE=57
    LTE=58
    MEASURE=59
    TEMPERATURE_VALUE=60
    AXIS_VALUE=61
    IDENTIFIER=62
    INTERGER=63
    DECIMAL=64
    WS=65
    BLOCK_COMMENT=66
    LINE_COMMENT=67
    GCODE_COMMENT=68

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
            self.state = 134
            self.statementList()
            self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.statement()
                self.state = 138
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.HOME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.simpleStatement()
                pass
            elif token in [GGCodeParser.AT, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.WHILE, GGCodeParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
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
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.MOVE, GGCodeParser.HOME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.motionStatement()
                pass
            elif token in [GGCodeParser.TEMPERATURE, GGCodeParser.WAIT, GGCodeParser.USE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.machineStatement()
                pass
            elif token in [GGCodeParser.ADD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.geometryStatement()
                pass
            elif token in [GGCodeParser.SET, GGCodeParser.DEFINE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
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


        def atBlockStatement(self):
            return self.getTypedRuleContext(GGCodeParser.AtBlockStatementContext,0)


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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.conditionalStatement()
                pass
            elif token in [GGCodeParser.REPEAT, GGCodeParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.loopStatement()
                pass
            elif token in [GGCodeParser.LBRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.blockStatement()
                pass
            elif token in [GGCodeParser.AT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.atBlockStatement()
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


        def homeStatement(self):
            return self.getTypedRuleContext(GGCodeParser.HomeStatementContext,0)


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
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MOVE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.moveStatement()
                pass
            elif token in [GGCodeParser.STOP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.stopStatement()
                pass
            elif token in [GGCodeParser.PAUSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.pauseStatement()
                pass
            elif token in [GGCodeParser.HOME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.homeStatement()
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
            self.state = 165
            self.match(GGCodeParser.MOVE)
            self.state = 166
            self.match(GGCodeParser.TO)
            self.state = 167
            self.moveTarget()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HomeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HOME(self):
            return self.getToken(GGCodeParser.HOME, 0)

        def axisList(self):
            return self.getTypedRuleContext(GGCodeParser.AxisListContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_homeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHomeStatement" ):
                listener.enterHomeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHomeStatement" ):
                listener.exitHomeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHomeStatement" ):
                return visitor.visitHomeStatement(self)
            else:
                return visitor.visitChildren(self)




    def homeStatement(self):

        localctx = GGCodeParser.HomeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_homeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GGCodeParser.HOME)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.T__0) | (1 << GGCodeParser.T__1) | (1 << GGCodeParser.T__2) | (1 << GGCodeParser.T__3))) != 0):
                self.state = 170
                self.axisList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def axis(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.AxisContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.AxisContext,i)


        def getRuleIndex(self):
            return GGCodeParser.RULE_axisList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxisList" ):
                listener.enterAxisList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxisList" ):
                listener.exitAxisList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxisList" ):
                return visitor.visitAxisList(self)
            else:
                return visitor.visitChildren(self)




    def axisList(self):

        localctx = GGCodeParser.AxisListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_axisList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.axis()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.T__0) | (1 << GGCodeParser.T__1) | (1 << GGCodeParser.T__2) | (1 << GGCodeParser.T__3))) != 0):
                self.state = 174
                self.axis()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GGCodeParser.RULE_axis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxis" ):
                listener.enterAxis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxis" ):
                listener.exitAxis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxis" ):
                return visitor.visitAxis(self)
            else:
                return visitor.visitChildren(self)




    def axis(self):

        localctx = GGCodeParser.AxisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_axis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.T__0) | (1 << GGCodeParser.T__1) | (1 << GGCodeParser.T__2) | (1 << GGCodeParser.T__3))) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_moveTarget)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MEASURE, GGCodeParser.AXIS_VALUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.coordinateTarget()
                pass
            elif token in [GGCodeParser.BASE, GGCodeParser.CENTER_POINT, GGCodeParser.ORIGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.pointTarget()
                pass
            elif token in [GGCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
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

        def axisSingle(self):
            return self.getTypedRuleContext(GGCodeParser.AxisSingleContext,0)


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
        self.enterRule(localctx, 22, self.RULE_coordinateTarget)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.axisSingle()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.axisPair()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.axisTriplet()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.measurePair()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.measureTriplet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisSingleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AXIS_VALUE(self):
            return self.getToken(GGCodeParser.AXIS_VALUE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_axisSingle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxisSingle" ):
                listener.enterAxisSingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxisSingle" ):
                listener.exitAxisSingle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxisSingle" ):
                return visitor.visitAxisSingle(self)
            else:
                return visitor.visitChildren(self)




    def axisSingle(self):

        localctx = GGCodeParser.AxisSingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_axisSingle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(GGCodeParser.AXIS_VALUE)
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
        self.enterRule(localctx, 26, self.RULE_axisPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(GGCodeParser.AXIS_VALUE)
            self.state = 197
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
        self.enterRule(localctx, 28, self.RULE_axisTriplet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(GGCodeParser.AXIS_VALUE)
            self.state = 200
            self.match(GGCodeParser.AXIS_VALUE)
            self.state = 201
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
        self.enterRule(localctx, 30, self.RULE_measurePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.measure()
            self.state = 204
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
        self.enterRule(localctx, 32, self.RULE_measureTriplet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.measure()
            self.state = 207
            self.measure()
            self.state = 208
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
        self.enterRule(localctx, 34, self.RULE_pointTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
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
        self.enterRule(localctx, 36, self.RULE_namedTarget)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
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
        self.enterRule(localctx, 38, self.RULE_stopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(GGCodeParser.STOP)
            self.state = 215
            self.match(GGCodeParser.AT)
            self.state = 216
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

        def anchorTarget(self):
            return self.getTypedRuleContext(GGCodeParser.AnchorTargetContext,0)


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
        self.enterRule(localctx, 40, self.RULE_pauseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(GGCodeParser.PAUSE)
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 219
                self.match(GGCodeParser.AT)
                self.state = 220
                self.anchorTarget()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnchorTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GGCodeParser.RULE_anchorTarget

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LayerAnchorContext(AnchorTargetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.AnchorTargetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAYER(self):
            return self.getToken(GGCodeParser.LAYER, 0)
        def INTERGER(self):
            return self.getToken(GGCodeParser.INTERGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayerAnchor" ):
                listener.enterLayerAnchor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayerAnchor" ):
                listener.exitLayerAnchor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLayerAnchor" ):
                return visitor.visitLayerAnchor(self)
            else:
                return visitor.visitChildren(self)


    class HeightAnchorContext(AnchorTargetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.AnchorTargetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEIGHT(self):
            return self.getToken(GGCodeParser.HEIGHT, 0)
        def measure(self):
            return self.getTypedRuleContext(GGCodeParser.MeasureContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeightAnchor" ):
                listener.enterHeightAnchor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeightAnchor" ):
                listener.exitHeightAnchor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeightAnchor" ):
                return visitor.visitHeightAnchor(self)
            else:
                return visitor.visitChildren(self)



    def anchorTarget(self):

        localctx = GGCodeParser.AnchorTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_anchorTarget)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.LAYER]:
                localctx = GGCodeParser.LayerAnchorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(GGCodeParser.LAYER)
                self.state = 224
                self.match(GGCodeParser.INTERGER)
                pass
            elif token in [GGCodeParser.HEIGHT]:
                localctx = GGCodeParser.HeightAnchorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(GGCodeParser.HEIGHT)
                self.state = 226
                self.measure()
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


    class AtBlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(GGCodeParser.AT, 0)

        def anchorTarget(self):
            return self.getTypedRuleContext(GGCodeParser.AnchorTargetContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(GGCodeParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_atBlockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtBlockStatement" ):
                listener.enterAtBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtBlockStatement" ):
                listener.exitAtBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtBlockStatement" ):
                return visitor.visitAtBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def atBlockStatement(self):

        localctx = GGCodeParser.AtBlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_atBlockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(GGCodeParser.AT)
            self.state = 230
            self.anchorTarget()
            self.state = 231
            self.blockStatement()
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
        self.enterRule(localctx, 46, self.RULE_machineStatement)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.TEMPERATURE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.temperatureStatement()
                pass
            elif token in [GGCodeParser.WAIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.waitStatement()
                pass
            elif token in [GGCodeParser.USE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
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
        self.enterRule(localctx, 48, self.RULE_temperatureStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(GGCodeParser.TEMPERATURE)
            self.state = 239
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
        self.enterRule(localctx, 50, self.RULE_waitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(GGCodeParser.WAIT)
            self.state = 242
            self.match(GGCodeParser.FOR)
            self.state = 243
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
        self.enterRule(localctx, 52, self.RULE_useStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(GGCodeParser.USE)
            self.state = 246
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
        self.enterRule(localctx, 54, self.RULE_durationValue)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(GGCodeParser.INTERGER)
                self.state = 249
                self.match(GGCodeParser.SECONDS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(GGCodeParser.INTERGER)
                self.state = 251
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
        self.enterRule(localctx, 56, self.RULE_temperatureValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 58, self.RULE_geometryStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
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
        self.enterRule(localctx, 60, self.RULE_addStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(GGCodeParser.ADD)
            self.state = 259
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
        self.enterRule(localctx, 62, self.RULE_shapeStatement)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.SQUARE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.squareStatement()
                pass
            elif token in [GGCodeParser.RECTANGLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.rectangleStatement()
                pass
            elif token in [GGCodeParser.CIRCLE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.circleStatement()
                pass
            elif token in [GGCodeParser.LINE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
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
        self.enterRule(localctx, 64, self.RULE_squareStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(GGCodeParser.SQUARE)
            self.state = 268
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
        self.enterRule(localctx, 66, self.RULE_squareParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.centerClause()
            self.state = 271
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
        self.enterRule(localctx, 68, self.RULE_rectangleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(GGCodeParser.RECTANGLE)
            self.state = 274
            self.centerClause()
            self.state = 275
            self.widthClause()
            self.state = 276
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
        self.enterRule(localctx, 70, self.RULE_circleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(GGCodeParser.CIRCLE)
            self.state = 279
            self.centerClause()
            self.state = 280
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
        self.enterRule(localctx, 72, self.RULE_lineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(GGCodeParser.LINE)
            self.state = 283
            self.fromClause()
            self.state = 284
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
        self.enterRule(localctx, 74, self.RULE_centerClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(GGCodeParser.CENTER)
            self.state = 287
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
        self.enterRule(localctx, 76, self.RULE_widthClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(GGCodeParser.WIDTH)
            self.state = 290
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
        self.enterRule(localctx, 78, self.RULE_lengthClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(GGCodeParser.LENGTH)
            self.state = 293
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
        self.enterRule(localctx, 80, self.RULE_radiusClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(GGCodeParser.RADIUS)
            self.state = 296
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
        self.enterRule(localctx, 82, self.RULE_fromClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(GGCodeParser.FROM)
            self.state = 299
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
        self.enterRule(localctx, 84, self.RULE_toClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(GGCodeParser.TO)
            self.state = 302
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
        self.enterRule(localctx, 86, self.RULE_coordinatePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.numericValue()
            self.state = 305
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
        self.enterRule(localctx, 88, self.RULE_definitionStatement)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.DEFINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.defineStatement()
                pass
            elif token in [GGCodeParser.SET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
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
        self.enterRule(localctx, 90, self.RULE_defineStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(GGCodeParser.DEFINE)
            self.state = 312
            self.match(GGCodeParser.IDENTIFIER)
            self.state = 313
            self.match(GGCodeParser.AS)
            self.state = 314
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
        self.enterRule(localctx, 92, self.RULE_locationDefinition)
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.INTERGER, GGCodeParser.DECIMAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.coordinatePair()
                pass
            elif token in [GGCodeParser.BASE, GGCodeParser.CENTER_POINT, GGCodeParser.ORIGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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
        self.enterRule(localctx, 94, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(GGCodeParser.SET)
            self.state = 321
            self.match(GGCodeParser.IDENTIFIER)
            self.state = 322
            self.match(GGCodeParser.TO)
            self.state = 323
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
        self.enterRule(localctx, 96, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(GGCodeParser.IF)
            self.state = 326
            self.condition()
            self.state = 327
            self.match(GGCodeParser.THEN)
            self.state = 328
            self.blockStatement()
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GGCodeParser.ELSE:
                self.state = 329
                self.match(GGCodeParser.ELSE)
                self.state = 330
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
        self.enterRule(localctx, 98, self.RULE_loopStatement)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.REPEAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(GGCodeParser.REPEAT)
                self.state = 334
                self.repeatCount()
                self.state = 335
                self.match(GGCodeParser.TIMES)
                self.state = 336
                self.blockStatement()
                pass
            elif token in [GGCodeParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(GGCodeParser.WHILE)
                self.state = 339
                self.condition()
                self.state = 340
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
        self.enterRule(localctx, 100, self.RULE_repeatCount)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
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
        self.enterRule(localctx, 102, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(GGCodeParser.LBRACE)
            self.state = 347
            self.statementList()
            self.state = 348
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
        self.enterRule(localctx, 104, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
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
        self.enterRule(localctx, 106, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
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
        self.enterRule(localctx, 108, self.RULE_comparisonExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.additiveExpression()
            self.state = 355
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
        self.enterRule(localctx, 110, self.RULE_comparisonTail)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.EQ, GGCodeParser.NEQ, GGCodeParser.GT, GGCodeParser.LT, GGCodeParser.GTE, GGCodeParser.LTE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.comparisonOperator()
                self.state = 358
                self.additiveExpression()
                self.state = 359
                self.comparisonTail()
                pass
            elif token in [GGCodeParser.EOF, GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.AT, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.THEN, GGCodeParser.WHILE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.HOME, GGCodeParser.RPAREN, GGCodeParser.LBRACE, GGCodeParser.RBRACE]:
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
        self.enterRule(localctx, 112, self.RULE_additiveExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.multiplicativeExpression()
            self.state = 365
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
        self.enterRule(localctx, 114, self.RULE_additiveTail)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.PLUS, GGCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.addOperator()
                self.state = 368
                self.multiplicativeExpression()
                self.state = 369
                self.additiveTail()
                pass
            elif token in [GGCodeParser.EOF, GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.AT, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.THEN, GGCodeParser.WHILE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.HOME, GGCodeParser.RPAREN, GGCodeParser.LBRACE, GGCodeParser.RBRACE, GGCodeParser.EQ, GGCodeParser.NEQ, GGCodeParser.GT, GGCodeParser.LT, GGCodeParser.GTE, GGCodeParser.LTE]:
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
        self.enterRule(localctx, 116, self.RULE_multiplicativeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.unaryExpression()
            self.state = 375
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
        self.enterRule(localctx, 118, self.RULE_multiplicativeTail)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.STAR, GGCodeParser.SLASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.mulOperator()
                self.state = 378
                self.unaryExpression()
                self.state = 379
                self.multiplicativeTail()
                pass
            elif token in [GGCodeParser.EOF, GGCodeParser.STOP, GGCodeParser.PAUSE, GGCodeParser.AT, GGCodeParser.TEMPERATURE, GGCodeParser.MOVE, GGCodeParser.ADD, GGCodeParser.SET, GGCodeParser.DEFINE, GGCodeParser.REPEAT, GGCodeParser.IF, GGCodeParser.THEN, GGCodeParser.WHILE, GGCodeParser.WAIT, GGCodeParser.USE, GGCodeParser.HOME, GGCodeParser.RPAREN, GGCodeParser.LBRACE, GGCodeParser.RBRACE, GGCodeParser.PLUS, GGCodeParser.MINUS, GGCodeParser.EQ, GGCodeParser.NEQ, GGCodeParser.GT, GGCodeParser.LT, GGCodeParser.GTE, GGCodeParser.LTE]:
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
        self.enterRule(localctx, 120, self.RULE_unaryExpression)
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(GGCodeParser.MINUS)
                self.state = 385
                self.unaryExpression()
                pass
            elif token in [GGCodeParser.LPAREN, GGCodeParser.IDENTIFIER, GGCodeParser.INTERGER, GGCodeParser.DECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
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
        self.enterRule(localctx, 122, self.RULE_primaryExpression)
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.INTERGER, GGCodeParser.DECIMAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.numericValue()
                pass
            elif token in [GGCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.match(GGCodeParser.IDENTIFIER)
                pass
            elif token in [GGCodeParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.match(GGCodeParser.LPAREN)
                self.state = 392
                self.expression()
                self.state = 393
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
        self.enterRule(localctx, 124, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
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
        self.enterRule(localctx, 126, self.RULE_addOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
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
        self.enterRule(localctx, 128, self.RULE_mulOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
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
        self.enterRule(localctx, 130, self.RULE_numericValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
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
        self.enterRule(localctx, 132, self.RULE_measure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(GGCodeParser.MEASURE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





