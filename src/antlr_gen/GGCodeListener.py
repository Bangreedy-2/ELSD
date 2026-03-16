# Generated from src/grammar/GGCode.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GGCodeParser import GGCodeParser
else:
    from GGCodeParser import GGCodeParser

# This class defines a complete listener for a parse tree produced by GGCodeParser.
class GGCodeListener(ParseTreeListener):

    # Enter a parse tree produced by GGCodeParser#program.
    def enterProgram(self, ctx:GGCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by GGCodeParser#program.
    def exitProgram(self, ctx:GGCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by GGCodeParser#statement.
    def enterStatement(self, ctx:GGCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#statement.
    def exitStatement(self, ctx:GGCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:GGCodeParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by GGCodeParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:GGCodeParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by GGCodeParser#assignment.
    def enterAssignment(self, ctx:GGCodeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GGCodeParser#assignment.
    def exitAssignment(self, ctx:GGCodeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GGCodeParser#moveStatement.
    def enterMoveStatement(self, ctx:GGCodeParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#moveStatement.
    def exitMoveStatement(self, ctx:GGCodeParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#ifStatement.
    def enterIfStatement(self, ctx:GGCodeParser.IfStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#ifStatement.
    def exitIfStatement(self, ctx:GGCodeParser.IfStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#repeatStatement.
    def enterRepeatStatement(self, ctx:GGCodeParser.RepeatStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#repeatStatement.
    def exitRepeatStatement(self, ctx:GGCodeParser.RepeatStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#block.
    def enterBlock(self, ctx:GGCodeParser.BlockContext):
        pass

    # Exit a parse tree produced by GGCodeParser#block.
    def exitBlock(self, ctx:GGCodeParser.BlockContext):
        pass


    # Enter a parse tree produced by GGCodeParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:GGCodeParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:GGCodeParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:GGCodeParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:GGCodeParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#relationalExpression.
    def enterRelationalExpression(self, ctx:GGCodeParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#relationalExpression.
    def exitRelationalExpression(self, ctx:GGCodeParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#equalityExpression.
    def enterEqualityExpression(self, ctx:GGCodeParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#equalityExpression.
    def exitEqualityExpression(self, ctx:GGCodeParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:GGCodeParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:GGCodeParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GGCodeParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GGCodeParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#primary.
    def enterPrimary(self, ctx:GGCodeParser.PrimaryContext):
        pass

    # Exit a parse tree produced by GGCodeParser#primary.
    def exitPrimary(self, ctx:GGCodeParser.PrimaryContext):
        pass



del GGCodeParser