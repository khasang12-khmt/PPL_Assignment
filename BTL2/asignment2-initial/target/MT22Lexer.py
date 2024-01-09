# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# KHA SANG - 2010576
from lexererr import *
import re



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\7\2\u0090\n\2\f\2\16\2\u0093")
        buf.write("\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009e\n")
        buf.write("\3\f\3\16\3\u00a1\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\5\63\u015d\n\63\3\63\3\63\3\63\5\63\u0162")
        buf.write("\n\63\3\63\3\63\5\63\u0166\n\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u016d\n\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\5\66\u0178\n\66\3\67\3\67\7\67\u017c\n\67\f")
        buf.write("\67\16\67\u017f\13\67\3\67\3\67\3\67\38\38\38\39\39\5")
        buf.write("9\u0189\n9\3:\3:\3:\3;\6;\u018f\n;\r;\16;\u0190\3;\3;")
        buf.write("\3<\3<\5<\u0197\n<\3<\3<\3<\7<\u019c\n<\f<\16<\u019f\13")
        buf.write("<\3=\3=\7=\u01a3\n=\f=\16=\u01a6\13=\3>\3>\5>\u01aa\n")
        buf.write(">\3>\6>\u01ad\n>\r>\16>\u01ae\3?\3?\5?\u01b3\n?\3?\7?")
        buf.write("\u01b6\n?\f?\16?\u01b9\13?\3@\3@\3A\3A\3B\3B\3C\3C\7C")
        buf.write("\u01c3\nC\fC\16C\u01c6\13C\3C\5C\u01c9\nC\3C\3C\3D\3D")
        buf.write("\7D\u01cf\nD\fD\16D\u01d2\13D\3D\3D\3D\3E\3E\3E\3\u0091")
        buf.write("\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2")
        buf.write("q\2s\2u9w:y\2{\2};\177\2\u0081\2\u0083\2\u0085<\u0087")
        buf.write("=\u0089>\3\2\f\4\2\f\f\17\17\n\2$$))^^ddhhppttvv\5\2\f")
        buf.write("\f\17\17$$\5\2\n\f\16\17\"\"\4\2GGgg\4\2--//\3\2\63;\4")
        buf.write("\2C\\c|\3\2\62;\4\3\f\f\17\17\2\u01e6\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3")
        buf.write("\u008b\3\2\2\2\5\u0099\3\2\2\2\7\u00a4\3\2\2\2\t\u00a9")
        buf.write("\3\2\2\2\13\u00af\3\2\2\2\r\u00b7\3\2\2\2\17\u00ba\3\2")
        buf.write("\2\2\21\u00bf\3\2\2\2\23\u00c5\3\2\2\2\25\u00cb\3\2\2")
        buf.write("\2\27\u00cf\3\2\2\2\31\u00d8\3\2\2\2\33\u00db\3\2\2\2")
        buf.write("\35\u00e3\3\2\2\2\37\u00ea\3\2\2\2!\u00f1\3\2\2\2#\u00f6")
        buf.write("\3\2\2\2%\u00fc\3\2\2\2\'\u0101\3\2\2\2)\u0105\3\2\2\2")
        buf.write("+\u010e\3\2\2\2-\u0111\3\2\2\2/\u0117\3\2\2\2\61\u011f")
        buf.write("\3\2\2\2\63\u0121\3\2\2\2\65\u0123\3\2\2\2\67\u0125\3")
        buf.write("\2\2\29\u0127\3\2\2\2;\u0129\3\2\2\2=\u012b\3\2\2\2?\u012e")
        buf.write("\3\2\2\2A\u0131\3\2\2\2C\u0134\3\2\2\2E\u0137\3\2\2\2")
        buf.write("G\u0139\3\2\2\2I\u013c\3\2\2\2K\u013e\3\2\2\2M\u0141\3")
        buf.write("\2\2\2O\u0144\3\2\2\2Q\u0146\3\2\2\2S\u0148\3\2\2\2U\u014a")
        buf.write("\3\2\2\2W\u014c\3\2\2\2Y\u014e\3\2\2\2[\u0150\3\2\2\2")
        buf.write("]\u0152\3\2\2\2_\u0154\3\2\2\2a\u0156\3\2\2\2c\u0158\3")
        buf.write("\2\2\2e\u016c\3\2\2\2g\u0170\3\2\2\2i\u0172\3\2\2\2k\u0177")
        buf.write("\3\2\2\2m\u0179\3\2\2\2o\u0183\3\2\2\2q\u0188\3\2\2\2")
        buf.write("s\u018a\3\2\2\2u\u018e\3\2\2\2w\u0196\3\2\2\2y\u01a0\3")
        buf.write("\2\2\2{\u01a7\3\2\2\2}\u01b0\3\2\2\2\177\u01ba\3\2\2\2")
        buf.write("\u0081\u01bc\3\2\2\2\u0083\u01be\3\2\2\2\u0085\u01c0\3")
        buf.write("\2\2\2\u0087\u01cc\3\2\2\2\u0089\u01d6\3\2\2\2\u008b\u008c")
        buf.write("\7\61\2\2\u008c\u008d\7,\2\2\u008d\u0091\3\2\2\2\u008e")
        buf.write("\u0090\13\2\2\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2")
        buf.write("\2\u0091\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7,\2\2\u0095")
        buf.write("\u0096\7\61\2\2\u0096\u0097\3\2\2\2\u0097\u0098\b\2\2")
        buf.write("\2\u0098\4\3\2\2\2\u0099\u009a\7\61\2\2\u009a\u009b\7")
        buf.write("\61\2\2\u009b\u009f\3\2\2\2\u009c\u009e\n\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3")
        buf.write("\2\2\2\u00a2\u00a3\b\3\2\2\u00a3\6\3\2\2\2\u00a4\u00a5")
        buf.write("\7c\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7m\2\2\u00ae\n\3\2\2\2\u00af\u00b0\7d\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7p\2\2\u00b6\f")
        buf.write("\3\2\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9\7q\2\2\u00b9\16")
        buf.write("\3\2\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7g\2\2\u00be\20\3\2\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\22\3\2\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7c\2\2\u00c9\u00ca\7v\2\2\u00ca\24\3\2\2\2\u00cb\u00cc")
        buf.write("\7h\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7t\2\2\u00ce\26")
        buf.write("\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7p\2\2\u00d7\30")
        buf.write("\3\2\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7h\2\2\u00da\32")
        buf.write("\3\2\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7i\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\u00e2\7t\2\2\u00e2\34\3\2\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7p\2\2\u00e9\36")
        buf.write("\3\2\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7i\2\2\u00f0 \3\2\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7g\2\2\u00f5\"")
        buf.write("\3\2\2\2\u00f6\u00f7\7y\2\2\u00f7\u00f8\7j\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7g\2\2\u00fb$\3")
        buf.write("\2\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7f\2\2\u0100&\3\2\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\u0103\7w\2\2\u0103\u0104\7v\2\2\u0104(\3")
        buf.write("\2\2\2\u0105\u0106\7e\2\2\u0106\u0107\7q\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7v\2\2\u0109\u010a\7k\2\2\u010a\u010b")
        buf.write("\7p\2\2\u010b\u010c\7w\2\2\u010c\u010d\7g\2\2\u010d*\3")
        buf.write("\2\2\2\u010e\u010f\7q\2\2\u010f\u0110\7h\2\2\u0110,\3")
        buf.write("\2\2\2\u0111\u0112\7c\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7t\2\2\u0114\u0115\7c\2\2\u0115\u0116\7{\2\2\u0116.\3")
        buf.write("\2\2\2\u0117\u0118\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a")
        buf.write("\7j\2\2\u011a\u011b\7g\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7v\2\2\u011e\60\3\2\2\2\u011f\u0120")
        buf.write("\7-\2\2\u0120\62\3\2\2\2\u0121\u0122\7/\2\2\u0122\64\3")
        buf.write("\2\2\2\u0123\u0124\7,\2\2\u0124\66\3\2\2\2\u0125\u0126")
        buf.write("\7\61\2\2\u01268\3\2\2\2\u0127\u0128\7\'\2\2\u0128:\3")
        buf.write("\2\2\2\u0129\u012a\7#\2\2\u012a<\3\2\2\2\u012b\u012c\7")
        buf.write("(\2\2\u012c\u012d\7(\2\2\u012d>\3\2\2\2\u012e\u012f\7")
        buf.write("~\2\2\u012f\u0130\7~\2\2\u0130@\3\2\2\2\u0131\u0132\7")
        buf.write("?\2\2\u0132\u0133\7?\2\2\u0133B\3\2\2\2\u0134\u0135\7")
        buf.write("#\2\2\u0135\u0136\7?\2\2\u0136D\3\2\2\2\u0137\u0138\7")
        buf.write(">\2\2\u0138F\3\2\2\2\u0139\u013a\7>\2\2\u013a\u013b\7")
        buf.write("?\2\2\u013bH\3\2\2\2\u013c\u013d\7@\2\2\u013dJ\3\2\2\2")
        buf.write("\u013e\u013f\7@\2\2\u013f\u0140\7?\2\2\u0140L\3\2\2\2")
        buf.write("\u0141\u0142\7<\2\2\u0142\u0143\7<\2\2\u0143N\3\2\2\2")
        buf.write("\u0144\u0145\7*\2\2\u0145P\3\2\2\2\u0146\u0147\7+\2\2")
        buf.write("\u0147R\3\2\2\2\u0148\u0149\7]\2\2\u0149T\3\2\2\2\u014a")
        buf.write("\u014b\7_\2\2\u014bV\3\2\2\2\u014c\u014d\7\60\2\2\u014d")
        buf.write("X\3\2\2\2\u014e\u014f\7.\2\2\u014fZ\3\2\2\2\u0150\u0151")
        buf.write("\7=\2\2\u0151\\\3\2\2\2\u0152\u0153\7<\2\2\u0153^\3\2")
        buf.write("\2\2\u0154\u0155\7}\2\2\u0155`\3\2\2\2\u0156\u0157\7\177")
        buf.write("\2\2\u0157b\3\2\2\2\u0158\u0159\7?\2\2\u0159d\3\2\2\2")
        buf.write("\u015a\u015d\5g\64\2\u015b\u015d\5i\65\2\u015c\u015a\3")
        buf.write("\2\2\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0161")
        buf.write("\5y=\2\u015f\u0162\5{>\2\u0160\u0162\3\2\2\2\u0161\u015f")
        buf.write("\3\2\2\2\u0161\u0160\3\2\2\2\u0162\u016d\3\2\2\2\u0163")
        buf.write("\u0166\5g\64\2\u0164\u0166\5i\65\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\5")
        buf.write("{>\2\u0168\u016d\3\2\2\2\u0169\u016a\5y=\2\u016a\u016b")
        buf.write("\5{>\2\u016b\u016d\3\2\2\2\u016c\u015c\3\2\2\2\u016c\u0165")
        buf.write("\3\2\2\2\u016c\u0169\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u016f\b\63\3\2\u016ff\3\2\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("h\3\2\2\2\u0172\u0173\5}?\2\u0173\u0174\b\65\4\2\u0174")
        buf.write("j\3\2\2\2\u0175\u0178\5!\21\2\u0176\u0178\5\21\t\2\u0177")
        buf.write("\u0175\3\2\2\2\u0177\u0176\3\2\2\2\u0178l\3\2\2\2\u0179")
        buf.write("\u017d\7$\2\2\u017a\u017c\5q9\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u0180\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\7")
        buf.write("$\2\2\u0181\u0182\b\67\5\2\u0182n\3\2\2\2\u0183\u0184")
        buf.write("\7^\2\2\u0184\u0185\t\3\2\2\u0185p\3\2\2\2\u0186\u0189")
        buf.write("\5o8\2\u0187\u0189\n\4\2\2\u0188\u0186\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189r\3\2\2\2\u018a\u018b\7^\2\2\u018b\u018c")
        buf.write("\n\3\2\2\u018ct\3\2\2\2\u018d\u018f\t\5\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\b;\2\2")
        buf.write("\u0193v\3\2\2\2\u0194\u0197\5\u0083B\2\u0195\u0197\5\177")
        buf.write("@\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u019d")
        buf.write("\3\2\2\2\u0198\u019c\5\177@\2\u0199\u019c\5\u0083B\2\u019a")
        buf.write("\u019c\5\u0081A\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2")
        buf.write("\2\2\u019b\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019ex\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u01a0\u01a4\7\60\2\2\u01a1\u01a3\5\u0081A\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5z\3\2\2\2\u01a6\u01a4\3\2\2")
        buf.write("\2\u01a7\u01a9\t\6\2\2\u01a8\u01aa\t\7\2\2\u01a9\u01a8")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab")
        buf.write("\u01ad\5\u0081A\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2")
        buf.write("\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af|\3")
        buf.write("\2\2\2\u01b0\u01b7\t\b\2\2\u01b1\u01b3\7a\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b6\5\u0081A\2\u01b5\u01b2\3\2\2\2\u01b6\u01b9\3\2")
        buf.write("\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8~\3")
        buf.write("\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bb\t\t\2\2\u01bb\u0080")
        buf.write("\3\2\2\2\u01bc\u01bd\t\n\2\2\u01bd\u0082\3\2\2\2\u01be")
        buf.write("\u01bf\7a\2\2\u01bf\u0084\3\2\2\2\u01c0\u01c4\7$\2\2\u01c1")
        buf.write("\u01c3\5q9\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c8\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c7\u01c9\t\13\2\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\bC\6\2\u01cb")
        buf.write("\u0086\3\2\2\2\u01cc\u01d0\7$\2\2\u01cd\u01cf\5q9\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3")
        buf.write("\2\2\2\u01d3\u01d4\5s:\2\u01d4\u01d5\bD\7\2\u01d5\u0088")
        buf.write("\3\2\2\2\u01d6\u01d7\13\2\2\2\u01d7\u01d8\bE\b\2\u01d8")
        buf.write("\u008a\3\2\2\2\30\2\u0091\u009f\u015c\u0161\u0165\u016c")
        buf.write("\u0177\u017d\u0188\u0190\u0196\u019b\u019d\u01a4\u01a9")
        buf.write("\u01ae\u01b2\u01b7\u01c4\u01c8\u01d0\t\b\2\2\3\63\2\3")
        buf.write("\65\3\3\67\4\3C\5\3D\6\3E\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    LINE_COMMENT = 2
    AUTO = 3
    BREAK = 4
    BOOLEAN = 5
    DO = 6
    ELSE = 7
    FALSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    TRUE = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    ARRAY = 22
    INHERIT = 23
    ADD = 24
    SUB = 25
    MUL = 26
    DIV = 27
    MOD = 28
    NOT = 29
    AND = 30
    OR = 31
    EQ = 32
    NEQ = 33
    LT = 34
    LTE = 35
    GT = 36
    GTE = 37
    CONCAT = 38
    LB = 39
    RB = 40
    LSB = 41
    RSB = 42
    DOT = 43
    COMMA = 44
    SEMICOLON = 45
    COLON = 46
    LP = 47
    RP = 48
    ASM = 49
    FLOAT_LIT = 50
    ZERO_LIT = 51
    INT_LIT = 52
    BOOL_LIT = 53
    STRING_LIT = 54
    WS = 55
    IDENTIFIER = 56
    INT_PART = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'array'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='", "'0'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "LINE_COMMENT", "AUTO", "BREAK", "BOOLEAN", "DO", 
            "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "ARRAY", "INHERIT", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "CONCAT", 
            "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", 
            "LP", "RP", "ASM", "FLOAT_LIT", "ZERO_LIT", "INT_LIT", "BOOL_LIT", 
            "STRING_LIT", "WS", "IDENTIFIER", "INT_PART", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "LINE_COMMENT", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "WHILE", "VOID", 
                  "OUT", "CONTINUE", "OF", "ARRAY", "INHERIT", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NEQ", 
                  "LT", "LTE", "GT", "GTE", "CONCAT", "LB", "RB", "LSB", 
                  "RSB", "DOT", "COMMA", "SEMICOLON", "COLON", "LP", "RP", 
                  "ASM", "FLOAT_LIT", "ZERO_LIT", "INT_LIT", "BOOL_LIT", 
                  "STRING_LIT", "VALID_ESC", "CHAR", "INVALID_ESC", "WS", 
                  "IDENTIFIER", "DEC_PART", "EXP_PART", "INT_PART", "LETTER", 
                  "DIGIT", "UNDERSCORE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.FLOAT_LIT_action 
            actions[51] = self.INT_LIT_action 
            actions[53] = self.STRING_LIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = re.sub('_','',self.text)
     

    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = re.sub('_','',self.text)
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                ESC = ['\r', '\n']
                text = str(self.text)
                raise UncloseString(text[1:]) 

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	illegal_str_from_beginning = str(self.text)
            	raise IllegalEscape(illegal_str_from_beginning[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


