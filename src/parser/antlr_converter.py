from typing import Any
from src.antlr_gen.GGCodeVisitor import GGCodeVisitor
from src.antlr_gen.GGCodeParser import GGCodeParser
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    VariableDeclaration, Assignment, MoveStatement, IfStatement,
    RepeatStatement, Block, Statement
)
from src.ast_nodes.expressions import (
    Expression, BinaryExpression, UnaryExpression, Literal, Identifier
)
from src.lexer.token_types import TokenType

class ASTBuilder(GGCodeVisitor):
    def visitProgram(self, ctx: GGCodeParser.ProgramContext):
        statements = []
        for i in range(ctx.getChildCount() - 1): # Last one is EOF
            child = ctx.getChild(i)
            res = self.visit(child)
            if res:
                statements.append(res)
        return Program(line=ctx.start.line, column=ctx.start.column, statements=statements)

    def visitStatement(self, ctx: GGCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))

    def visitVariableDeclaration(self, ctx: GGCodeParser.VariableDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.expression())
        return VariableDeclaration(
            line=ctx.start.line,
            column=ctx.start.column,
            identifier=identifier,
            expression=expr
        )

    def visitAssignment(self, ctx: GGCodeParser.AssignmentContext):
        identifier = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.expression())
        return Assignment(
            line=ctx.start.line,
            column=ctx.start.column,
            identifier=identifier,
            expression=expr
        )

    def visitMoveStatement(self, ctx: GGCodeParser.MoveStatementContext):
        exprs = ctx.expression()
        return MoveStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            x=self.visit(exprs[0]),
            y=self.visit(exprs[1])
        )

    def visitIfStatement(self, ctx: GGCodeParser.IfStatementContext):
        cond = self.visit(ctx.expression())
        blocks = ctx.block()
        then_branch = self.visit(blocks[0])
        else_branch = self.visit(blocks[1]) if len(blocks) > 1 else None
        return IfStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            condition=cond,
            then_branch=then_branch,
            else_branch=else_branch
        )

    def visitRepeatStatement(self, ctx: GGCodeParser.RepeatStatementContext):
        count = self.visit(ctx.expression())
        body = self.visit(ctx.block())
        return RepeatStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            count=count,
            body=body
        )

    def visitBlock(self, ctx: GGCodeParser.BlockContext):
        stmts = []
        # children are LBRACE, stmt*, RBRACE
        for i in range(1, ctx.getChildCount() - 1):
            stmts.append(self.visit(ctx.getChild(i)))
        return Block(
            line=ctx.start.line,
            column=ctx.start.column,
            statements=stmts
        )

    # Expressions
    def visitUnaryExpression(self, ctx: GGCodeParser.UnaryExpressionContext):
        operand = self.visit(ctx.expression())
        return UnaryExpression(
            line=ctx.start.line,
            column=ctx.start.column,
            operator=TokenType.MINUS,
            operand=operand
        )

    def visitMultiplicativeExpression(self, ctx: GGCodeParser.MultiplicativeExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op_token = ctx.getChild(1).getSymbol()
        op_type = TokenType.STAR if op_token.type == GGCodeParser.STAR else TokenType.SLASH
        return BinaryExpression(
            line=ctx.start.line,
            column=ctx.start.column,
            left=left,
            operator=op_type,
            right=right
        )

    def visitAdditiveExpression(self, ctx: GGCodeParser.AdditiveExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op_token = ctx.getChild(1).getSymbol()
        op_type = TokenType.PLUS if op_token.type == GGCodeParser.PLUS else TokenType.MINUS
        return BinaryExpression(
            line=ctx.start.line,
            column=ctx.start.column,
            left=left,
            operator=op_type,
            right=right
        )

    def visitRelationalExpression(self, ctx: GGCodeParser.RelationalExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op_token = ctx.getChild(1).getSymbol()
        msg = {
            GGCodeParser.GT: TokenType.GT,
            GGCodeParser.LT: TokenType.LT,
            GGCodeParser.GTE: TokenType.GTE,
            GGCodeParser.LTE: TokenType.LTE
        }
        return BinaryExpression(
            line=ctx.start.line,
            column=ctx.start.column,
            left=left,
            operator=msg[op_token.type],
            right=right
        )

    def visitEqualityExpression(self, ctx: GGCodeParser.EqualityExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op_token = ctx.getChild(1).getSymbol()
        op = TokenType.EQ if op_token.type == GGCodeParser.EQ else TokenType.NEQ
        return BinaryExpression(
            line=ctx.start.line,
            column=ctx.start.column,
            left=left,
            operator=op,
            right=right
        )

    def visitPrimaryExpression(self, ctx: GGCodeParser.PrimaryExpressionContext):
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: GGCodeParser.PrimaryContext):
        if ctx.NUMBER():
            val = float(ctx.NUMBER().getText())
            if val.is_integer(): val = int(val)
            return Literal(line=ctx.start.line, column=ctx.start.column, value=val)
        elif ctx.BOOLEAN():
            val = ctx.BOOLEAN().getText() == 'true'
            return Literal(line=ctx.start.line, column=ctx.start.column, value=val)
        elif ctx.IDENTIFIER():
            return Identifier(line=ctx.start.line, column=ctx.start.column, name=ctx.IDENTIFIER().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())

