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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\6\62\u0164\n\62\r\62\16\62\u0165\3\62\3\62\6\62")
        buf.write("\u016a\n\62\r\62\16\62\u016b\5\62\u016e\n\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u0174\n\62\3\63\6\63\u0177\n\63\r\63\16")
        buf.write("\63\u0178\3\63\3\63\3\64\3\64\5\64\u017f\n\64\3\64\6\64")
        buf.write("\u0182\n\64\r\64\16\64\u0183\3\64\3\64\6\64\u0188\n\64")
        buf.write("\r\64\16\64\u0189\5\64\u018c\n\64\3\65\3\65\7\65\u0190")
        buf.write("\n\65\f\65\16\65\u0193\13\65\3\66\6\66\u0196\n\66\r\66")
        buf.write("\16\66\u0197\3\67\6\67\u019b\n\67\r\67\16\67\u019c\3\67")
        buf.write("\3\67\6\67\u01a1\n\67\r\67\16\67\u01a2\38\68\u01a6\n8")
        buf.write("\r8\168\u01a7\38\38\39\39\39\39\79\u01b0\n9\f9\169\u01b3")
        buf.write("\139\39\39\39\39\39\3:\3:\3:\3:\7:\u01be\n:\f:\16:\u01c1")
        buf.write("\13:\3:\3:\3\u01b1\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;\3\2\36\4\2UUuu\4\2VVvv\4\2QQqq\4")
        buf.write("\2RRrr\4\2CCcc\4\2WWww\4\2GGgg\4\2NNnn\4\2[[{{\4\2TTt")
        buf.write("t\4\2OOoo\4\2XXxx\4\2FFff\4\2SSss\4\2EEee\4\2PPpp\4\2")
        buf.write("IIii\4\2JJjj\4\2YYyy\4\2KKkk\4\2HHhh\4\2DDdd\3\2\62;\4")
        buf.write("\2Z\\z|\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4")
        buf.write("\2\f\f\17\17\2\u01d3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5z\3")
        buf.write("\2\2\2\7\u0080\3\2\2\2\t\u0083\3\2\2\2\13\u0089\3\2\2")
        buf.write("\2\r\u0095\3\2\2\2\17\u009a\3\2\2\2\21\u009d\3\2\2\2\23")
        buf.write("\u00a1\3\2\2\2\25\u00a8\3\2\2\2\27\u00af\3\2\2\2\31\u00b6")
        buf.write("\3\2\2\2\33\u00bc\3\2\2\2\35\u00c6\3\2\2\2\37\u00cd\3")
        buf.write("\2\2\2!\u00d4\3\2\2\2#\u00d9\3\2\2\2%\u00de\3\2\2\2\'")
        buf.write("\u00e3\3\2\2\2)\u00f0\3\2\2\2+\u00f7\3\2\2\2-\u00fb\3")
        buf.write("\2\2\2/\u0102\3\2\2\2\61\u0105\3\2\2\2\63\u010c\3\2\2")
        buf.write("\2\65\u0112\3\2\2\2\67\u0115\3\2\2\29\u011a\3\2\2\2;\u011f")
        buf.write("\3\2\2\2=\u0125\3\2\2\2?\u012a\3\2\2\2A\u012e\3\2\2\2")
        buf.write("C\u0136\3\2\2\2E\u013e\3\2\2\2G\u0142\3\2\2\2I\u0144\3")
        buf.write("\2\2\2K\u0146\3\2\2\2M\u0148\3\2\2\2O\u014a\3\2\2\2Q\u014c")
        buf.write("\3\2\2\2S\u014e\3\2\2\2U\u0150\3\2\2\2W\u0152\3\2\2\2")
        buf.write("Y\u0155\3\2\2\2[\u0158\3\2\2\2]\u015a\3\2\2\2_\u015c\3")
        buf.write("\2\2\2a\u015f\3\2\2\2c\u0163\3\2\2\2e\u0176\3\2\2\2g\u017c")
        buf.write("\3\2\2\2i\u018d\3\2\2\2k\u0195\3\2\2\2m\u019a\3\2\2\2")
        buf.write("o\u01a5\3\2\2\2q\u01ab\3\2\2\2s\u01b9\3\2\2\2uv\t\2\2")
        buf.write("\2vw\t\3\2\2wx\t\4\2\2xy\t\5\2\2y\4\3\2\2\2z{\t\5\2\2")
        buf.write("{|\t\6\2\2|}\t\7\2\2}~\t\2\2\2~\177\t\b\2\2\177\6\3\2")
        buf.write("\2\2\u0080\u0081\t\6\2\2\u0081\u0082\t\3\2\2\u0082\b\3")
        buf.write("\2\2\2\u0083\u0084\t\t\2\2\u0084\u0085\t\6\2\2\u0085\u0086")
        buf.write("\t\n\2\2\u0086\u0087\t\b\2\2\u0087\u0088\t\13\2\2\u0088")
        buf.write("\n\3\2\2\2\u0089\u008a\t\3\2\2\u008a\u008b\t\b\2\2\u008b")
        buf.write("\u008c\t\f\2\2\u008c\u008d\t\5\2\2\u008d\u008e\t\b\2\2")
        buf.write("\u008e\u008f\t\13\2\2\u008f\u0090\t\6\2\2\u0090\u0091")
        buf.write("\t\3\2\2\u0091\u0092\t\7\2\2\u0092\u0093\t\13\2\2\u0093")
        buf.write("\u0094\t\b\2\2\u0094\f\3\2\2\2\u0095\u0096\t\f\2\2\u0096")
        buf.write("\u0097\t\4\2\2\u0097\u0098\t\r\2\2\u0098\u0099\t\b\2\2")
        buf.write("\u0099\16\3\2\2\2\u009a\u009b\t\3\2\2\u009b\u009c\t\4")
        buf.write("\2\2\u009c\20\3\2\2\2\u009d\u009e\t\6\2\2\u009e\u009f")
        buf.write("\t\16\2\2\u009f\u00a0\t\16\2\2\u00a0\22\3\2\2\2\u00a1")
        buf.write("\u00a2\t\2\2\2\u00a2\u00a3\t\17\2\2\u00a3\u00a4\t\7\2")
        buf.write("\2\u00a4\u00a5\t\6\2\2\u00a5\u00a6\t\13\2\2\u00a6\u00a7")
        buf.write("\t\b\2\2\u00a7\24\3\2\2\2\u00a8\u00a9\t\20\2\2\u00a9\u00aa")
        buf.write("\t\b\2\2\u00aa\u00ab\t\21\2\2\u00ab\u00ac\t\3\2\2\u00ac")
        buf.write("\u00ad\t\b\2\2\u00ad\u00ae\t\13\2\2\u00ae\26\3\2\2\2\u00af")
        buf.write("\u00b0\t\t\2\2\u00b0\u00b1\t\b\2\2\u00b1\u00b2\t\21\2")
        buf.write("\2\u00b2\u00b3\t\22\2\2\u00b3\u00b4\t\3\2\2\u00b4\u00b5")
        buf.write("\t\23\2\2\u00b5\30\3\2\2\2\u00b6\u00b7\t\24\2\2\u00b7")
        buf.write("\u00b8\t\25\2\2\u00b8\u00b9\t\16\2\2\u00b9\u00ba\t\3\2")
        buf.write("\2\u00ba\u00bb\t\23\2\2\u00bb\32\3\2\2\2\u00bc\u00bd\t")
        buf.write("\13\2\2\u00bd\u00be\t\b\2\2\u00be\u00bf\t\20\2\2\u00bf")
        buf.write("\u00c0\t\3\2\2\u00c0\u00c1\t\6\2\2\u00c1\u00c2\t\21\2")
        buf.write("\2\u00c2\u00c3\t\22\2\2\u00c3\u00c4\t\t\2\2\u00c4\u00c5")
        buf.write("\t\b\2\2\u00c5\34\3\2\2\2\u00c6\u00c7\t\20\2\2\u00c7\u00c8")
        buf.write("\t\25\2\2\u00c8\u00c9\t\13\2\2\u00c9\u00ca\t\20\2\2\u00ca")
        buf.write("\u00cb\t\t\2\2\u00cb\u00cc\t\b\2\2\u00cc\36\3\2\2\2\u00cd")
        buf.write("\u00ce\t\13\2\2\u00ce\u00cf\t\6\2\2\u00cf\u00d0\t\16\2")
        buf.write("\2\u00d0\u00d1\t\25\2\2\u00d1\u00d2\t\7\2\2\u00d2\u00d3")
        buf.write("\t\2\2\2\u00d3 \3\2\2\2\u00d4\u00d5\t\t\2\2\u00d5\u00d6")
        buf.write("\t\25\2\2\u00d6\u00d7\t\21\2\2\u00d7\u00d8\t\b\2\2\u00d8")
        buf.write("\"\3\2\2\2\u00d9\u00da\t\26\2\2\u00da\u00db\t\13\2\2\u00db")
        buf.write("\u00dc\t\4\2\2\u00dc\u00dd\t\f\2\2\u00dd$\3\2\2\2\u00de")
        buf.write("\u00df\t\27\2\2\u00df\u00e0\t\6\2\2\u00e0\u00e1\t\2\2")
        buf.write("\2\u00e1\u00e2\t\b\2\2\u00e2&\3\2\2\2\u00e3\u00e4\t\20")
        buf.write("\2\2\u00e4\u00e5\t\b\2\2\u00e5\u00e6\t\21\2\2\u00e6\u00e7")
        buf.write("\t\3\2\2\u00e7\u00e8\t\b\2\2\u00e8\u00e9\t\13\2\2\u00e9")
        buf.write("\u00ea\7a\2\2\u00ea\u00eb\t\5\2\2\u00eb\u00ec\t\4\2\2")
        buf.write("\u00ec\u00ed\t\25\2\2\u00ed\u00ee\t\21\2\2\u00ee\u00ef")
        buf.write("\t\3\2\2\u00ef(\3\2\2\2\u00f0\u00f1\t\4\2\2\u00f1\u00f2")
        buf.write("\t\13\2\2\u00f2\u00f3\t\25\2\2\u00f3\u00f4\t\22\2\2\u00f4")
        buf.write("\u00f5\t\25\2\2\u00f5\u00f6\t\21\2\2\u00f6*\3\2\2\2\u00f7")
        buf.write("\u00f8\t\2\2\2\u00f8\u00f9\t\b\2\2\u00f9\u00fa\t\3\2\2")
        buf.write("\u00fa,\3\2\2\2\u00fb\u00fc\t\16\2\2\u00fc\u00fd\t\b\2")
        buf.write("\2\u00fd\u00fe\t\26\2\2\u00fe\u00ff\t\25\2\2\u00ff\u0100")
        buf.write("\t\21\2\2\u0100\u0101\t\b\2\2\u0101.\3\2\2\2\u0102\u0103")
        buf.write("\t\6\2\2\u0103\u0104\t\2\2\2\u0104\60\3\2\2\2\u0105\u0106")
        buf.write("\t\13\2\2\u0106\u0107\t\b\2\2\u0107\u0108\t\5\2\2\u0108")
        buf.write("\u0109\t\b\2\2\u0109\u010a\t\6\2\2\u010a\u010b\t\3\2\2")
        buf.write("\u010b\62\3\2\2\2\u010c\u010d\t\3\2\2\u010d\u010e\t\25")
        buf.write("\2\2\u010e\u010f\t\f\2\2\u010f\u0110\t\b\2\2\u0110\u0111")
        buf.write("\t\2\2\2\u0111\64\3\2\2\2\u0112\u0113\t\25\2\2\u0113\u0114")
        buf.write("\t\26\2\2\u0114\66\3\2\2\2\u0115\u0116\t\3\2\2\u0116\u0117")
        buf.write("\t\23\2\2\u0117\u0118\t\b\2\2\u0118\u0119\t\21\2\2\u0119")
        buf.write("8\3\2\2\2\u011a\u011b\t\b\2\2\u011b\u011c\t\t\2\2\u011c")
        buf.write("\u011d\t\2\2\2\u011d\u011e\t\b\2\2\u011e:\3\2\2\2\u011f")
        buf.write("\u0120\t\24\2\2\u0120\u0121\t\23\2\2\u0121\u0122\t\25")
        buf.write("\2\2\u0122\u0123\t\t\2\2\u0123\u0124\t\b\2\2\u0124<\3")
        buf.write("\2\2\2\u0125\u0126\t\24\2\2\u0126\u0127\t\6\2\2\u0127")
        buf.write("\u0128\t\25\2\2\u0128\u0129\t\3\2\2\u0129>\3\2\2\2\u012a")
        buf.write("\u012b\t\26\2\2\u012b\u012c\t\4\2\2\u012c\u012d\t\13\2")
        buf.write("\2\u012d@\3\2\2\2\u012e\u012f\t\2\2\2\u012f\u0130\t\b")
        buf.write("\2\2\u0130\u0131\t\20\2\2\u0131\u0132\t\4\2\2\u0132\u0133")
        buf.write("\t\21\2\2\u0133\u0134\t\16\2\2\u0134\u0135\t\2\2\2\u0135")
        buf.write("B\3\2\2\2\u0136\u0137\t\f\2\2\u0137\u0138\t\25\2\2\u0138")
        buf.write("\u0139\t\21\2\2\u0139\u013a\t\7\2\2\u013a\u013b\t\3\2")
        buf.write("\2\u013b\u013c\t\b\2\2\u013c\u013d\t\2\2\2\u013dD\3\2")
        buf.write("\2\2\u013e\u013f\t\7\2\2\u013f\u0140\t\2\2\2\u0140\u0141")
        buf.write("\t\b\2\2\u0141F\3\2\2\2\u0142\u0143\7*\2\2\u0143H\3\2")
        buf.write("\2\2\u0144\u0145\7+\2\2\u0145J\3\2\2\2\u0146\u0147\7}")
        buf.write("\2\2\u0147L\3\2\2\2\u0148\u0149\7\177\2\2\u0149N\3\2\2")
        buf.write("\2\u014a\u014b\7-\2\2\u014bP\3\2\2\2\u014c\u014d\7/\2")
        buf.write("\2\u014dR\3\2\2\2\u014e\u014f\7,\2\2\u014fT\3\2\2\2\u0150")
        buf.write("\u0151\7\61\2\2\u0151V\3\2\2\2\u0152\u0153\7?\2\2\u0153")
        buf.write("\u0154\7?\2\2\u0154X\3\2\2\2\u0155\u0156\7#\2\2\u0156")
        buf.write("\u0157\7?\2\2\u0157Z\3\2\2\2\u0158\u0159\7@\2\2\u0159")
        buf.write("\\\3\2\2\2\u015a\u015b\7>\2\2\u015b^\3\2\2\2\u015c\u015d")
        buf.write("\7@\2\2\u015d\u015e\7?\2\2\u015e`\3\2\2\2\u015f\u0160")
        buf.write("\7>\2\2\u0160\u0161\7?\2\2\u0161b\3\2\2\2\u0162\u0164")
        buf.write("\t\30\2\2\u0163\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u016d\3\2\2\2")
        buf.write("\u0167\u0169\7\60\2\2\u0168\u016a\t\30\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u0167\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0173\3\2\2\2\u016f\u0170\7")
        buf.write("o\2\2\u0170\u0174\7o\2\2\u0171\u0172\7e\2\2\u0172\u0174")
        buf.write("\7o\2\2\u0173\u016f\3\2\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write("d\3\2\2\2\u0175\u0177\t\30\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017b\t\20\2\2\u017bf\3\2\2")
        buf.write("\2\u017c\u017e\t\31\2\2\u017d\u017f\7/\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180")
        buf.write("\u0182\t\30\2\2\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2")
        buf.write("\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u018b")
        buf.write("\3\2\2\2\u0185\u0187\7\60\2\2\u0186\u0188\t\30\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0185\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018ch\3\2\2\2\u018d\u0191")
        buf.write("\t\32\2\2\u018e\u0190\t\33\2\2\u018f\u018e\3\2\2\2\u0190")
        buf.write("\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2")
        buf.write("\u0192j\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\t\30\2")
        buf.write("\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198l\3\2\2\2\u0199\u019b")
        buf.write("\t\30\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u01a0\7\60\2\2\u019f\u01a1\t\30\2\2\u01a0\u019f")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3n\3\2\2\2\u01a4\u01a6\t\34\2\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\b")
        buf.write("8\2\2\u01aap\3\2\2\2\u01ab\u01ac\7\61\2\2\u01ac\u01ad")
        buf.write("\7,\2\2\u01ad\u01b1\3\2\2\2\u01ae\u01b0\13\2\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01b2\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b4\u01b5\7,\2\2\u01b5\u01b6\7\61\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b8\b9\2\2\u01b8r\3\2\2\2\u01b9\u01ba")
        buf.write("\7\61\2\2\u01ba\u01bb\7\61\2\2\u01bb\u01bf\3\2\2\2\u01bc")
        buf.write("\u01be\n\35\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1\3\2\2")
        buf.write("\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\b:\2\2\u01c3")
        buf.write("t\3\2\2\2\23\2\u0165\u016b\u016d\u0173\u0178\u017e\u0183")
        buf.write("\u0189\u018b\u0191\u0197\u019c\u01a2\u01a7\u01b1\u01bf")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class GGCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STOP = 1
    PAUSE = 2
    AT = 3
    LAYER = 4
    TEMPERATURE = 5
    MOVE = 6
    TO = 7
    ADD = 8
    SQUARE = 9
    CENTER = 10
    LENGTH = 11
    WIDTH = 12
    RECTANGLE = 13
    CIRCLE = 14
    RADIUS = 15
    LINE = 16
    FROM = 17
    BASE = 18
    CENTER_POINT = 19
    ORIGIN = 20
    SET = 21
    DEFINE = 22
    AS = 23
    REPEAT = 24
    TIMES = 25
    IF = 26
    THEN = 27
    ELSE = 28
    WHILE = 29
    WAIT = 30
    FOR = 31
    SECONDS = 32
    MINUTES = 33
    USE = 34
    LPAREN = 35
    RPAREN = 36
    LBRACE = 37
    RBRACE = 38
    PLUS = 39
    MINUS = 40
    STAR = 41
    SLASH = 42
    EQ = 43
    NEQ = 44
    GT = 45
    LT = 46
    GTE = 47
    LTE = 48
    MEASURE = 49
    TEMPERATURE_VALUE = 50
    AXIS_VALUE = 51
    IDENTIFIER = 52
    INTERGER = 53
    DECIMAL = 54
    WS = 55
    BLOCK_COMMENT = 56
    LINE_COMMENT = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "STOP", "PAUSE", "AT", "LAYER", "TEMPERATURE", "MOVE", "TO", 
            "ADD", "SQUARE", "CENTER", "LENGTH", "WIDTH", "RECTANGLE", "CIRCLE", 
            "RADIUS", "LINE", "FROM", "BASE", "CENTER_POINT", "ORIGIN", 
            "SET", "DEFINE", "AS", "REPEAT", "TIMES", "IF", "THEN", "ELSE", 
            "WHILE", "WAIT", "FOR", "SECONDS", "MINUTES", "USE", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", "SLASH", 
            "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "MEASURE", "TEMPERATURE_VALUE", 
            "AXIS_VALUE", "IDENTIFIER", "INTERGER", "DECIMAL", "WS", "BLOCK_COMMENT", 
            "LINE_COMMENT" ]

    ruleNames = [ "STOP", "PAUSE", "AT", "LAYER", "TEMPERATURE", "MOVE", 
                  "TO", "ADD", "SQUARE", "CENTER", "LENGTH", "WIDTH", "RECTANGLE", 
                  "CIRCLE", "RADIUS", "LINE", "FROM", "BASE", "CENTER_POINT", 
                  "ORIGIN", "SET", "DEFINE", "AS", "REPEAT", "TIMES", "IF", 
                  "THEN", "ELSE", "WHILE", "WAIT", "FOR", "SECONDS", "MINUTES", 
                  "USE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", 
                  "MINUS", "STAR", "SLASH", "EQ", "NEQ", "GT", "LT", "GTE", 
                  "LTE", "MEASURE", "TEMPERATURE_VALUE", "AXIS_VALUE", "IDENTIFIER", 
                  "INTERGER", "DECIMAL", "WS", "BLOCK_COMMENT", "LINE_COMMENT" ]

    grammarFileName = "GGCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


