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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("r\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7A\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\7\tK\n\t\f\t\16\tN")
        buf.write("\13\t\3\t\3\t\3\n\3\n\3\n\3\n\5\nV\n\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nd\n\n\f\n\16\ng\13")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13p\n\13\3\13")
        buf.write("\2\3\22\f\2\4\6\b\n\f\16\20\22\24\2\6\3\2\23\24\3\2\21")
        buf.write("\22\3\2\27\32\3\2\25\26\2w\2\31\3\2\2\2\4$\3\2\2\2\6&")
        buf.write("\3\2\2\2\b,\3\2\2\2\n\61\3\2\2\2\f9\3\2\2\2\16B\3\2\2")
        buf.write("\2\20H\3\2\2\2\22U\3\2\2\2\24o\3\2\2\2\26\30\5\4\3\2\27")
        buf.write("\26\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7\2\2\3\35\3\3\2\2")
        buf.write("\2\36%\5\6\4\2\37%\5\b\5\2 %\5\n\6\2!%\5\f\7\2\"%\5\16")
        buf.write("\b\2#%\5\20\t\2$\36\3\2\2\2$\37\3\2\2\2$ \3\2\2\2$!\3")
        buf.write("\2\2\2$\"\3\2\2\2$#\3\2\2\2%\5\3\2\2\2&\'\7\3\2\2\'(\7")
        buf.write("\33\2\2()\7\20\2\2)*\5\22\n\2*+\7\17\2\2+\7\3\2\2\2,-")
        buf.write("\7\33\2\2-.\7\20\2\2./\5\22\n\2/\60\7\17\2\2\60\t\3\2")
        buf.write("\2\2\61\62\7\4\2\2\62\63\7\n\2\2\63\64\5\22\n\2\64\65")
        buf.write("\7\16\2\2\65\66\5\22\n\2\66\67\7\13\2\2\678\7\17\2\28")
        buf.write("\13\3\2\2\29:\7\5\2\2:;\7\n\2\2;<\5\22\n\2<=\7\13\2\2")
        buf.write("=@\5\20\t\2>?\7\6\2\2?A\5\20\t\2@>\3\2\2\2@A\3\2\2\2A")
        buf.write("\r\3\2\2\2BC\7\7\2\2CD\7\n\2\2DE\5\22\n\2EF\7\13\2\2F")
        buf.write("G\5\20\t\2G\17\3\2\2\2HL\7\f\2\2IK\5\4\3\2JI\3\2\2\2K")
        buf.write("N\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2OP\7")
        buf.write("\r\2\2P\21\3\2\2\2QR\b\n\1\2RS\7\22\2\2SV\5\22\n\bTV\5")
        buf.write("\24\13\2UQ\3\2\2\2UT\3\2\2\2Ve\3\2\2\2WX\f\7\2\2XY\t\2")
        buf.write("\2\2Yd\5\22\n\bZ[\f\6\2\2[\\\t\3\2\2\\d\5\22\n\7]^\f\5")
        buf.write("\2\2^_\t\4\2\2_d\5\22\n\6`a\f\4\2\2ab\t\5\2\2bd\5\22\n")
        buf.write("\5cW\3\2\2\2cZ\3\2\2\2c]\3\2\2\2c`\3\2\2\2dg\3\2\2\2e")
        buf.write("c\3\2\2\2ef\3\2\2\2f\23\3\2\2\2ge\3\2\2\2hp\7\34\2\2i")
        buf.write("p\7\35\2\2jp\7\33\2\2kl\7\n\2\2lm\5\22\n\2mn\7\13\2\2")
        buf.write("np\3\2\2\2oh\3\2\2\2oi\3\2\2\2oj\3\2\2\2ok\3\2\2\2p\25")
        buf.write("\3\2\2\2\n\31$@LUceo")
        return buf.getvalue()


class GGCodeParser ( Parser ):

    grammarFileName = "GGCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'move'", "'if'", "'else'", "'repeat'", 
                     "'true'", "'false'", "'('", "')'", "'{'", "'}'", "','", 
                     "';'", "'='", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "LET", "MOVE", "IF", "ELSE", "REPEAT", 
                      "TRUE", "FALSE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COMMA", "SEMI", "ASSIGN", "PLUS", "MINUS", "STAR", 
                      "SLASH", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "IDENTIFIER", 
                      "NUMBER", "BOOLEAN", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_assignment = 3
    RULE_moveStatement = 4
    RULE_ifStatement = 5
    RULE_repeatStatement = 6
    RULE_block = 7
    RULE_expression = 8
    RULE_primary = 9

    ruleNames =  [ "program", "statement", "variableDeclaration", "assignment", 
                   "moveStatement", "ifStatement", "repeatStatement", "block", 
                   "expression", "primary" ]

    EOF = Token.EOF
    LET=1
    MOVE=2
    IF=3
    ELSE=4
    REPEAT=5
    TRUE=6
    FALSE=7
    LPAREN=8
    RPAREN=9
    LBRACE=10
    RBRACE=11
    COMMA=12
    SEMI=13
    ASSIGN=14
    PLUS=15
    MINUS=16
    STAR=17
    SLASH=18
    EQ=19
    NEQ=20
    GT=21
    LT=22
    GTE=23
    LTE=24
    IDENTIFIER=25
    NUMBER=26
    BOOLEAN=27
    WS=28
    COMMENT=29
    BLOCK_COMMENT=30

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

        def EOF(self):
            return self.getToken(GGCodeParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.StatementContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.LET) | (1 << GGCodeParser.MOVE) | (1 << GGCodeParser.IF) | (1 << GGCodeParser.REPEAT) | (1 << GGCodeParser.LBRACE) | (1 << GGCodeParser.IDENTIFIER))) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(GGCodeParser.EOF)
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

        def variableDeclaration(self):
            return self.getTypedRuleContext(GGCodeParser.VariableDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GGCodeParser.AssignmentContext,0)


        def moveStatement(self):
            return self.getTypedRuleContext(GGCodeParser.MoveStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(GGCodeParser.IfStatementContext,0)


        def repeatStatement(self):
            return self.getTypedRuleContext(GGCodeParser.RepeatStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(GGCodeParser.BlockContext,0)


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
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.LET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.variableDeclaration()
                pass
            elif token in [GGCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.assignment()
                pass
            elif token in [GGCodeParser.MOVE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.moveStatement()
                pass
            elif token in [GGCodeParser.IF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.ifStatement()
                pass
            elif token in [GGCodeParser.REPEAT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.repeatStatement()
                pass
            elif token in [GGCodeParser.LBRACE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.block()
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


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(GGCodeParser.LET, 0)

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(GGCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(GGCodeParser.SEMI, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = GGCodeParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GGCodeParser.LET)
            self.state = 37
            self.match(GGCodeParser.IDENTIFIER)
            self.state = 38
            self.match(GGCodeParser.ASSIGN)
            self.state = 39
            self.expression(0)
            self.state = 40
            self.match(GGCodeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(GGCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(GGCodeParser.SEMI, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GGCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GGCodeParser.IDENTIFIER)
            self.state = 43
            self.match(GGCodeParser.ASSIGN)
            self.state = 44
            self.expression(0)
            self.state = 45
            self.match(GGCodeParser.SEMI)
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

        def LPAREN(self):
            return self.getToken(GGCodeParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(GGCodeParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(GGCodeParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(GGCodeParser.SEMI, 0)

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
        self.enterRule(localctx, 8, self.RULE_moveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(GGCodeParser.MOVE)
            self.state = 48
            self.match(GGCodeParser.LPAREN)
            self.state = 49
            self.expression(0)
            self.state = 50
            self.match(GGCodeParser.COMMA)
            self.state = 51
            self.expression(0)
            self.state = 52
            self.match(GGCodeParser.RPAREN)
            self.state = 53
            self.match(GGCodeParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GGCodeParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GGCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GGCodeParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.BlockContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(GGCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = GGCodeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(GGCodeParser.IF)
            self.state = 56
            self.match(GGCodeParser.LPAREN)
            self.state = 57
            self.expression(0)
            self.state = 58
            self.match(GGCodeParser.RPAREN)
            self.state = 59
            self.block()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GGCodeParser.ELSE:
                self.state = 60
                self.match(GGCodeParser.ELSE)
                self.state = 61
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(GGCodeParser.REPEAT, 0)

        def LPAREN(self):
            return self.getToken(GGCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GGCodeParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(GGCodeParser.BlockContext,0)


        def getRuleIndex(self):
            return GGCodeParser.RULE_repeatStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatStatement" ):
                listener.enterRepeatStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatStatement" ):
                listener.exitRepeatStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatStatement" ):
                return visitor.visitRepeatStatement(self)
            else:
                return visitor.visitChildren(self)




    def repeatStatement(self):

        localctx = GGCodeParser.RepeatStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_repeatStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(GGCodeParser.REPEAT)
            self.state = 65
            self.match(GGCodeParser.LPAREN)
            self.state = 66
            self.expression(0)
            self.state = 67
            self.match(GGCodeParser.RPAREN)
            self.state = 68
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(GGCodeParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GGCodeParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return GGCodeParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = GGCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(GGCodeParser.LBRACE)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.LET) | (1 << GGCodeParser.MOVE) | (1 << GGCodeParser.IF) | (1 << GGCodeParser.REPEAT) | (1 << GGCodeParser.LBRACE) | (1 << GGCodeParser.IDENTIFIER))) != 0):
                self.state = 71
                self.statement()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(GGCodeParser.RBRACE)
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


        def getRuleIndex(self):
            return GGCodeParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PrimaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(GGCodeParser.PrimaryContext,0)


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


    class AdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(GGCodeParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(GGCodeParser.MINUS, 0)

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


    class RelationalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.ExpressionContext,i)

        def GT(self):
            return self.getToken(GGCodeParser.GT, 0)
        def LT(self):
            return self.getToken(GGCodeParser.LT, 0)
        def GTE(self):
            return self.getToken(GGCodeParser.GTE, 0)
        def LTE(self):
            return self.getToken(GGCodeParser.LTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(GGCodeParser.EQ, 0)
        def NEQ(self):
            return self.getToken(GGCodeParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GGCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GGCodeParser.ExpressionContext,i)

        def STAR(self):
            return self.getToken(GGCodeParser.STAR, 0)
        def SLASH(self):
            return self.getToken(GGCodeParser.SLASH, 0)

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


    class UnaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GGCodeParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(GGCodeParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


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



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GGCodeParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.MINUS]:
                localctx = GGCodeParser.UnaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(GGCodeParser.MINUS)
                self.state = 81
                self.expression(6)
                pass
            elif token in [GGCodeParser.LPAREN, GGCodeParser.IDENTIFIER, GGCodeParser.NUMBER, GGCodeParser.BOOLEAN]:
                localctx = GGCodeParser.PrimaryExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 82
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 97
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = GGCodeParser.MultiplicativeExpressionContext(self, GGCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 85
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not(_la==GGCodeParser.STAR or _la==GGCodeParser.SLASH):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = GGCodeParser.AdditiveExpressionContext(self, GGCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 88
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 89
                        _la = self._input.LA(1)
                        if not(_la==GGCodeParser.PLUS or _la==GGCodeParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = GGCodeParser.RelationalExpressionContext(self, GGCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 91
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 92
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GGCodeParser.GT) | (1 << GGCodeParser.LT) | (1 << GGCodeParser.GTE) | (1 << GGCodeParser.LTE))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 93
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = GGCodeParser.EqualityExpressionContext(self, GGCodeParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 94
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 95
                        _la = self._input.LA(1)
                        if not(_la==GGCodeParser.EQ or _la==GGCodeParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.expression(3)
                        pass

             
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(GGCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(GGCodeParser.BOOLEAN, 0)

        def IDENTIFIER(self):
            return self.getToken(GGCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(GGCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(GGCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(GGCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return GGCodeParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = GGCodeParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primary)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GGCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(GGCodeParser.NUMBER)
                pass
            elif token in [GGCodeParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(GGCodeParser.BOOLEAN)
                pass
            elif token in [GGCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(GGCodeParser.IDENTIFIER)
                pass
            elif token in [GGCodeParser.LPAREN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.match(GGCodeParser.LPAREN)
                self.state = 106
                self.expression(0)
                self.state = 107
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




