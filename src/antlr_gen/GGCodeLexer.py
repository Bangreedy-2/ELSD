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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u01ff\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3:\3;\3;\3;\3<\6<\u0196\n<\r<\16<\u0197\3<")
        buf.write("\3<\6<\u019c\n<\r<\16<\u019d\5<\u01a0\n<\3<\3<\3<\3<\5")
        buf.write("<\u01a6\n<\3=\6=\u01a9\n=\r=\16=\u01aa\3=\3=\3>\3>\5>")
        buf.write("\u01b1\n>\3>\6>\u01b4\n>\r>\16>\u01b5\3>\3>\6>\u01ba\n")
        buf.write(">\r>\16>\u01bb\5>\u01be\n>\3?\3?\7?\u01c2\n?\f?\16?\u01c5")
        buf.write("\13?\3@\6@\u01c8\n@\r@\16@\u01c9\3A\6A\u01cd\nA\rA\16")
        buf.write("A\u01ce\3A\3A\6A\u01d3\nA\rA\16A\u01d4\3B\6B\u01d8\nB")
        buf.write("\rB\16B\u01d9\3B\3B\3C\3C\3C\3C\7C\u01e2\nC\fC\16C\u01e5")
        buf.write("\13C\3C\3C\3C\3C\3C\3D\3D\3D\3D\7D\u01f0\nD\fD\16D\u01f3")
        buf.write("\13D\3D\3D\3E\3E\7E\u01f9\nE\fE\16E\u01fc\13E\3E\3E\3")
        buf.write("\u01e3\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\3\2 \4\2UUuu\4\2VVvv\4\2QQqq\4\2RRrr\4\2CCcc")
        buf.write("\4\2WWww\4\2GGgg\4\2NNnn\4\2[[{{\4\2TTtt\4\2JJjj\4\2K")
        buf.write("Kkk\4\2IIii\4\2OOoo\4\2XXxx\4\2FFff\4\2SSss\4\2EEee\4")
        buf.write("\2PPpp\4\2YYyy\4\2HHhh\4\2DDdd\4\2ZZzz\4\2\\\\||\3\2\62")
        buf.write(";\6\2GGZ\\ggz|\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\4\2\f\f\17\17\2\u020f\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2\2\5\u008d")
        buf.write("\3\2\2\2\7\u008f\3\2\2\2\t\u0091\3\2\2\2\13\u0093\3\2")
        buf.write("\2\2\r\u0098\3\2\2\2\17\u009e\3\2\2\2\21\u00a1\3\2\2\2")
        buf.write("\23\u00a7\3\2\2\2\25\u00ae\3\2\2\2\27\u00ba\3\2\2\2\31")
        buf.write("\u00bf\3\2\2\2\33\u00c2\3\2\2\2\35\u00c6\3\2\2\2\37\u00cd")
        buf.write("\3\2\2\2!\u00d4\3\2\2\2#\u00db\3\2\2\2%\u00e1\3\2\2\2")
        buf.write("\'\u00eb\3\2\2\2)\u00f2\3\2\2\2+\u00f9\3\2\2\2-\u00fe")
        buf.write("\3\2\2\2/\u0103\3\2\2\2\61\u0108\3\2\2\2\63\u0115\3\2")
        buf.write("\2\2\65\u011c\3\2\2\2\67\u0120\3\2\2\29\u0127\3\2\2\2")
        buf.write(";\u012a\3\2\2\2=\u0131\3\2\2\2?\u0137\3\2\2\2A\u013a\3")
        buf.write("\2\2\2C\u013f\3\2\2\2E\u0144\3\2\2\2G\u014a\3\2\2\2I\u014f")
        buf.write("\3\2\2\2K\u0153\3\2\2\2M\u015b\3\2\2\2O\u0163\3\2\2\2")
        buf.write("Q\u0167\3\2\2\2S\u016c\3\2\2\2U\u016e\3\2\2\2W\u0170\3")
        buf.write("\2\2\2Y\u0172\3\2\2\2[\u0174\3\2\2\2]\u0176\3\2\2\2_\u0178")
        buf.write("\3\2\2\2a\u017a\3\2\2\2c\u017c\3\2\2\2e\u017e\3\2\2\2")
        buf.write("g\u0180\3\2\2\2i\u0182\3\2\2\2k\u0184\3\2\2\2m\u0187\3")
        buf.write("\2\2\2o\u018a\3\2\2\2q\u018c\3\2\2\2s\u018e\3\2\2\2u\u0191")
        buf.write("\3\2\2\2w\u0195\3\2\2\2y\u01a8\3\2\2\2{\u01ae\3\2\2\2")
        buf.write("}\u01bf\3\2\2\2\177\u01c7\3\2\2\2\u0081\u01cc\3\2\2\2")
        buf.write("\u0083\u01d7\3\2\2\2\u0085\u01dd\3\2\2\2\u0087\u01eb\3")
        buf.write("\2\2\2\u0089\u01f6\3\2\2\2\u008b\u008c\7Z\2\2\u008c\4")
        buf.write("\3\2\2\2\u008d\u008e\7[\2\2\u008e\6\3\2\2\2\u008f\u0090")
        buf.write("\7\\\2\2\u0090\b\3\2\2\2\u0091\u0092\7G\2\2\u0092\n\3")
        buf.write("\2\2\2\u0093\u0094\t\2\2\2\u0094\u0095\t\3\2\2\u0095\u0096")
        buf.write("\t\4\2\2\u0096\u0097\t\5\2\2\u0097\f\3\2\2\2\u0098\u0099")
        buf.write("\t\5\2\2\u0099\u009a\t\6\2\2\u009a\u009b\t\7\2\2\u009b")
        buf.write("\u009c\t\2\2\2\u009c\u009d\t\b\2\2\u009d\16\3\2\2\2\u009e")
        buf.write("\u009f\t\6\2\2\u009f\u00a0\t\3\2\2\u00a0\20\3\2\2\2\u00a1")
        buf.write("\u00a2\t\t\2\2\u00a2\u00a3\t\6\2\2\u00a3\u00a4\t\n\2\2")
        buf.write("\u00a4\u00a5\t\b\2\2\u00a5\u00a6\t\13\2\2\u00a6\22\3\2")
        buf.write("\2\2\u00a7\u00a8\t\f\2\2\u00a8\u00a9\t\b\2\2\u00a9\u00aa")
        buf.write("\t\r\2\2\u00aa\u00ab\t\16\2\2\u00ab\u00ac\t\f\2\2\u00ac")
        buf.write("\u00ad\t\3\2\2\u00ad\24\3\2\2\2\u00ae\u00af\t\3\2\2\u00af")
        buf.write("\u00b0\t\b\2\2\u00b0\u00b1\t\17\2\2\u00b1\u00b2\t\5\2")
        buf.write("\2\u00b2\u00b3\t\b\2\2\u00b3\u00b4\t\13\2\2\u00b4\u00b5")
        buf.write("\t\6\2\2\u00b5\u00b6\t\3\2\2\u00b6\u00b7\t\7\2\2\u00b7")
        buf.write("\u00b8\t\13\2\2\u00b8\u00b9\t\b\2\2\u00b9\26\3\2\2\2\u00ba")
        buf.write("\u00bb\t\17\2\2\u00bb\u00bc\t\4\2\2\u00bc\u00bd\t\20\2")
        buf.write("\2\u00bd\u00be\t\b\2\2\u00be\30\3\2\2\2\u00bf\u00c0\t")
        buf.write("\3\2\2\u00c0\u00c1\t\4\2\2\u00c1\32\3\2\2\2\u00c2\u00c3")
        buf.write("\t\6\2\2\u00c3\u00c4\t\21\2\2\u00c4\u00c5\t\21\2\2\u00c5")
        buf.write("\34\3\2\2\2\u00c6\u00c7\t\2\2\2\u00c7\u00c8\t\22\2\2\u00c8")
        buf.write("\u00c9\t\7\2\2\u00c9\u00ca\t\6\2\2\u00ca\u00cb\t\13\2")
        buf.write("\2\u00cb\u00cc\t\b\2\2\u00cc\36\3\2\2\2\u00cd\u00ce\t")
        buf.write("\23\2\2\u00ce\u00cf\t\b\2\2\u00cf\u00d0\t\24\2\2\u00d0")
        buf.write("\u00d1\t\3\2\2\u00d1\u00d2\t\b\2\2\u00d2\u00d3\t\13\2")
        buf.write("\2\u00d3 \3\2\2\2\u00d4\u00d5\t\t\2\2\u00d5\u00d6\t\b")
        buf.write("\2\2\u00d6\u00d7\t\24\2\2\u00d7\u00d8\t\16\2\2\u00d8\u00d9")
        buf.write("\t\3\2\2\u00d9\u00da\t\f\2\2\u00da\"\3\2\2\2\u00db\u00dc")
        buf.write("\t\25\2\2\u00dc\u00dd\t\r\2\2\u00dd\u00de\t\21\2\2\u00de")
        buf.write("\u00df\t\3\2\2\u00df\u00e0\t\f\2\2\u00e0$\3\2\2\2\u00e1")
        buf.write("\u00e2\t\13\2\2\u00e2\u00e3\t\b\2\2\u00e3\u00e4\t\23\2")
        buf.write("\2\u00e4\u00e5\t\3\2\2\u00e5\u00e6\t\6\2\2\u00e6\u00e7")
        buf.write("\t\24\2\2\u00e7\u00e8\t\16\2\2\u00e8\u00e9\t\t\2\2\u00e9")
        buf.write("\u00ea\t\b\2\2\u00ea&\3\2\2\2\u00eb\u00ec\t\23\2\2\u00ec")
        buf.write("\u00ed\t\r\2\2\u00ed\u00ee\t\13\2\2\u00ee\u00ef\t\23\2")
        buf.write("\2\u00ef\u00f0\t\t\2\2\u00f0\u00f1\t\b\2\2\u00f1(\3\2")
        buf.write("\2\2\u00f2\u00f3\t\13\2\2\u00f3\u00f4\t\6\2\2\u00f4\u00f5")
        buf.write("\t\21\2\2\u00f5\u00f6\t\r\2\2\u00f6\u00f7\t\7\2\2\u00f7")
        buf.write("\u00f8\t\2\2\2\u00f8*\3\2\2\2\u00f9\u00fa\t\t\2\2\u00fa")
        buf.write("\u00fb\t\r\2\2\u00fb\u00fc\t\24\2\2\u00fc\u00fd\t\b\2")
        buf.write("\2\u00fd,\3\2\2\2\u00fe\u00ff\t\26\2\2\u00ff\u0100\t\13")
        buf.write("\2\2\u0100\u0101\t\4\2\2\u0101\u0102\t\17\2\2\u0102.\3")
        buf.write("\2\2\2\u0103\u0104\t\27\2\2\u0104\u0105\t\6\2\2\u0105")
        buf.write("\u0106\t\2\2\2\u0106\u0107\t\b\2\2\u0107\60\3\2\2\2\u0108")
        buf.write("\u0109\t\23\2\2\u0109\u010a\t\b\2\2\u010a\u010b\t\24\2")
        buf.write("\2\u010b\u010c\t\3\2\2\u010c\u010d\t\b\2\2\u010d\u010e")
        buf.write("\t\13\2\2\u010e\u010f\7a\2\2\u010f\u0110\t\5\2\2\u0110")
        buf.write("\u0111\t\4\2\2\u0111\u0112\t\r\2\2\u0112\u0113\t\24\2")
        buf.write("\2\u0113\u0114\t\3\2\2\u0114\62\3\2\2\2\u0115\u0116\t")
        buf.write("\4\2\2\u0116\u0117\t\13\2\2\u0117\u0118\t\r\2\2\u0118")
        buf.write("\u0119\t\16\2\2\u0119\u011a\t\r\2\2\u011a\u011b\t\24\2")
        buf.write("\2\u011b\64\3\2\2\2\u011c\u011d\t\2\2\2\u011d\u011e\t")
        buf.write("\b\2\2\u011e\u011f\t\3\2\2\u011f\66\3\2\2\2\u0120\u0121")
        buf.write("\t\21\2\2\u0121\u0122\t\b\2\2\u0122\u0123\t\26\2\2\u0123")
        buf.write("\u0124\t\r\2\2\u0124\u0125\t\24\2\2\u0125\u0126\t\b\2")
        buf.write("\2\u01268\3\2\2\2\u0127\u0128\t\6\2\2\u0128\u0129\t\2")
        buf.write("\2\2\u0129:\3\2\2\2\u012a\u012b\t\13\2\2\u012b\u012c\t")
        buf.write("\b\2\2\u012c\u012d\t\5\2\2\u012d\u012e\t\b\2\2\u012e\u012f")
        buf.write("\t\6\2\2\u012f\u0130\t\3\2\2\u0130<\3\2\2\2\u0131\u0132")
        buf.write("\t\3\2\2\u0132\u0133\t\r\2\2\u0133\u0134\t\17\2\2\u0134")
        buf.write("\u0135\t\b\2\2\u0135\u0136\t\2\2\2\u0136>\3\2\2\2\u0137")
        buf.write("\u0138\t\r\2\2\u0138\u0139\t\26\2\2\u0139@\3\2\2\2\u013a")
        buf.write("\u013b\t\3\2\2\u013b\u013c\t\f\2\2\u013c\u013d\t\b\2\2")
        buf.write("\u013d\u013e\t\24\2\2\u013eB\3\2\2\2\u013f\u0140\t\b\2")
        buf.write("\2\u0140\u0141\t\t\2\2\u0141\u0142\t\2\2\2\u0142\u0143")
        buf.write("\t\b\2\2\u0143D\3\2\2\2\u0144\u0145\t\25\2\2\u0145\u0146")
        buf.write("\t\f\2\2\u0146\u0147\t\r\2\2\u0147\u0148\t\t\2\2\u0148")
        buf.write("\u0149\t\b\2\2\u0149F\3\2\2\2\u014a\u014b\t\25\2\2\u014b")
        buf.write("\u014c\t\6\2\2\u014c\u014d\t\r\2\2\u014d\u014e\t\3\2\2")
        buf.write("\u014eH\3\2\2\2\u014f\u0150\t\26\2\2\u0150\u0151\t\4\2")
        buf.write("\2\u0151\u0152\t\13\2\2\u0152J\3\2\2\2\u0153\u0154\t\2")
        buf.write("\2\2\u0154\u0155\t\b\2\2\u0155\u0156\t\23\2\2\u0156\u0157")
        buf.write("\t\4\2\2\u0157\u0158\t\24\2\2\u0158\u0159\t\21\2\2\u0159")
        buf.write("\u015a\t\2\2\2\u015aL\3\2\2\2\u015b\u015c\t\17\2\2\u015c")
        buf.write("\u015d\t\r\2\2\u015d\u015e\t\24\2\2\u015e\u015f\t\7\2")
        buf.write("\2\u015f\u0160\t\3\2\2\u0160\u0161\t\b\2\2\u0161\u0162")
        buf.write("\t\2\2\2\u0162N\3\2\2\2\u0163\u0164\t\7\2\2\u0164\u0165")
        buf.write("\t\2\2\2\u0165\u0166\t\b\2\2\u0166P\3\2\2\2\u0167\u0168")
        buf.write("\t\f\2\2\u0168\u0169\t\4\2\2\u0169\u016a\t\17\2\2\u016a")
        buf.write("\u016b\t\b\2\2\u016bR\3\2\2\2\u016c\u016d\t\30\2\2\u016d")
        buf.write("T\3\2\2\2\u016e\u016f\t\n\2\2\u016fV\3\2\2\2\u0170\u0171")
        buf.write("\t\31\2\2\u0171X\3\2\2\2\u0172\u0173\t\b\2\2\u0173Z\3")
        buf.write("\2\2\2\u0174\u0175\7*\2\2\u0175\\\3\2\2\2\u0176\u0177")
        buf.write("\7+\2\2\u0177^\3\2\2\2\u0178\u0179\7}\2\2\u0179`\3\2\2")
        buf.write("\2\u017a\u017b\7\177\2\2\u017bb\3\2\2\2\u017c\u017d\7")
        buf.write("-\2\2\u017dd\3\2\2\2\u017e\u017f\7/\2\2\u017ff\3\2\2\2")
        buf.write("\u0180\u0181\7,\2\2\u0181h\3\2\2\2\u0182\u0183\7\61\2")
        buf.write("\2\u0183j\3\2\2\2\u0184\u0185\7?\2\2\u0185\u0186\7?\2")
        buf.write("\2\u0186l\3\2\2\2\u0187\u0188\7#\2\2\u0188\u0189\7?\2")
        buf.write("\2\u0189n\3\2\2\2\u018a\u018b\7@\2\2\u018bp\3\2\2\2\u018c")
        buf.write("\u018d\7>\2\2\u018dr\3\2\2\2\u018e\u018f\7@\2\2\u018f")
        buf.write("\u0190\7?\2\2\u0190t\3\2\2\2\u0191\u0192\7>\2\2\u0192")
        buf.write("\u0193\7?\2\2\u0193v\3\2\2\2\u0194\u0196\t\32\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198\u019f\3\2\2\2\u0199\u019b\7")
        buf.write("\60\2\2\u019a\u019c\t\32\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u01a0\3\2\2\2\u019f\u0199\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0\u01a5\3\2\2\2\u01a1\u01a2\7o\2\2\u01a2\u01a6")
        buf.write("\7o\2\2\u01a3\u01a4\7e\2\2\u01a4\u01a6\7o\2\2\u01a5\u01a1")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6x\3\2\2\2\u01a7\u01a9")
        buf.write("\t\32\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ac\u01ad\t\23\2\2\u01adz\3\2\2\2\u01ae\u01b0\t\33")
        buf.write("\2\2\u01af\u01b1\7/\2\2\u01b0\u01af\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b4\t\32\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01bd\3\2\2\2\u01b7\u01b9\7")
        buf.write("\60\2\2\u01b8\u01ba\t\32\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01be\3\2\2\2\u01bd\u01b7\3\2\2\2\u01bd\u01be\3")
        buf.write("\2\2\2\u01be|\3\2\2\2\u01bf\u01c3\t\34\2\2\u01c0\u01c2")
        buf.write("\t\35\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4~\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c6\u01c8\t\32\2\2\u01c7\u01c6\3\2\2")
        buf.write("\2\u01c8\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u0080\3\2\2\2\u01cb\u01cd\t\32\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2\7")
        buf.write("\60\2\2\u01d1\u01d3\t\32\2\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u0082\3\2\2\2\u01d6\u01d8\t\36\2\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\bB\2\2")
        buf.write("\u01dc\u0084\3\2\2\2\u01dd\u01de\7\61\2\2\u01de\u01df")
        buf.write("\7,\2\2\u01df\u01e3\3\2\2\2\u01e0\u01e2\13\2\2\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e4\u01e6\3\2\2\2\u01e5\u01e3\3")
        buf.write("\2\2\2\u01e6\u01e7\7,\2\2\u01e7\u01e8\7\61\2\2\u01e8\u01e9")
        buf.write("\3\2\2\2\u01e9\u01ea\bC\2\2\u01ea\u0086\3\2\2\2\u01eb")
        buf.write("\u01ec\7\61\2\2\u01ec\u01ed\7\61\2\2\u01ed\u01f1\3\2\2")
        buf.write("\2\u01ee\u01f0\n\37\2\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3")
        buf.write("\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2")
        buf.write("\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\bD\2\2")
        buf.write("\u01f5\u0088\3\2\2\2\u01f6\u01fa\7=\2\2\u01f7\u01f9\n")
        buf.write("\37\2\2\u01f8\u01f7\3\2\2\2\u01f9\u01fc\3\2\2\2\u01fa")
        buf.write("\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2")
        buf.write("\u01fc\u01fa\3\2\2\2\u01fd\u01fe\bE\2\2\u01fe\u008a\3")
        buf.write("\2\2\2\24\2\u0197\u019d\u019f\u01a5\u01aa\u01b0\u01b5")
        buf.write("\u01bb\u01bd\u01c3\u01c9\u01ce\u01d4\u01d9\u01e3\u01f1")
        buf.write("\u01fa\3\b\2\2")
        return buf.getvalue()


class GGCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    STOP = 5
    PAUSE = 6
    AT = 7
    LAYER = 8
    HEIGHT = 9
    TEMPERATURE = 10
    MOVE = 11
    TO = 12
    ADD = 13
    SQUARE = 14
    CENTER = 15
    LENGTH = 16
    WIDTH = 17
    RECTANGLE = 18
    CIRCLE = 19
    RADIUS = 20
    LINE = 21
    FROM = 22
    BASE = 23
    CENTER_POINT = 24
    ORIGIN = 25
    SET = 26
    DEFINE = 27
    AS = 28
    REPEAT = 29
    TIMES = 30
    IF = 31
    THEN = 32
    ELSE = 33
    WHILE = 34
    WAIT = 35
    FOR = 36
    SECONDS = 37
    MINUTES = 38
    USE = 39
    HOME = 40
    KEY_X = 41
    KEY_Y = 42
    KEY_Z = 43
    KEY_E = 44
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    PLUS = 49
    MINUS = 50
    STAR = 51
    SLASH = 52
    EQ = 53
    NEQ = 54
    GT = 55
    LT = 56
    GTE = 57
    LTE = 58
    MEASURE = 59
    TEMPERATURE_VALUE = 60
    AXIS_VALUE = 61
    IDENTIFIER = 62
    INTERGER = 63
    DECIMAL = 64
    WS = 65
    BLOCK_COMMENT = 66
    LINE_COMMENT = 67
    GCODE_COMMENT = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'X'", "'Y'", "'Z'", "'E'", "'('", "')'", "'{'", "'}'", "'+'", 
            "'-'", "'*'", "'/'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>",
            "STOP", "PAUSE", "AT", "LAYER", "HEIGHT", "TEMPERATURE", "MOVE", 
            "TO", "ADD", "SQUARE", "CENTER", "LENGTH", "WIDTH", "RECTANGLE", 
            "CIRCLE", "RADIUS", "LINE", "FROM", "BASE", "CENTER_POINT", 
            "ORIGIN", "SET", "DEFINE", "AS", "REPEAT", "TIMES", "IF", "THEN", 
            "ELSE", "WHILE", "WAIT", "FOR", "SECONDS", "MINUTES", "USE", 
            "HOME", "KEY_X", "KEY_Y", "KEY_Z", "KEY_E", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", "SLASH", "EQ", 
            "NEQ", "GT", "LT", "GTE", "LTE", "MEASURE", "TEMPERATURE_VALUE", 
            "AXIS_VALUE", "IDENTIFIER", "INTERGER", "DECIMAL", "WS", "BLOCK_COMMENT", 
            "LINE_COMMENT", "GCODE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "STOP", "PAUSE", "AT", 
                  "LAYER", "HEIGHT", "TEMPERATURE", "MOVE", "TO", "ADD", 
                  "SQUARE", "CENTER", "LENGTH", "WIDTH", "RECTANGLE", "CIRCLE", 
                  "RADIUS", "LINE", "FROM", "BASE", "CENTER_POINT", "ORIGIN", 
                  "SET", "DEFINE", "AS", "REPEAT", "TIMES", "IF", "THEN", 
                  "ELSE", "WHILE", "WAIT", "FOR", "SECONDS", "MINUTES", 
                  "USE", "HOME", "KEY_X", "KEY_Y", "KEY_Z", "KEY_E", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "STAR", 
                  "SLASH", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "MEASURE", 
                  "TEMPERATURE_VALUE", "AXIS_VALUE", "IDENTIFIER", "INTERGER", 
                  "DECIMAL", "WS", "BLOCK_COMMENT", "LINE_COMMENT", "GCODE_COMMENT" ]

    grammarFileName = "GGCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


