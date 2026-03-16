# Generated from src/grammar/GGCode.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GGCodeParser import GGCodeParser
else:
    from GGCodeParser import GGCodeParser

# This class defines a complete generic visitor for a parse tree produced by GGCodeParser.

class GGCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GGCodeParser#program.
    def visitProgram(self, ctx:GGCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#statement.
    def visitStatement(self, ctx:GGCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:GGCodeParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#assignment.
    def visitAssignment(self, ctx:GGCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#moveStatement.
    def visitMoveStatement(self, ctx:GGCodeParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#ifStatement.
    def visitIfStatement(self, ctx:GGCodeParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#repeatStatement.
    def visitRepeatStatement(self, ctx:GGCodeParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#block.
    def visitBlock(self, ctx:GGCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:GGCodeParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:GGCodeParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#relationalExpression.
    def visitRelationalExpression(self, ctx:GGCodeParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#equalityExpression.
    def visitEqualityExpression(self, ctx:GGCodeParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:GGCodeParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#unaryExpression.
    def visitUnaryExpression(self, ctx:GGCodeParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#primary.
    def visitPrimary(self, ctx:GGCodeParser.PrimaryContext):
        return self.visitChildren(ctx)



del GGCodeParser