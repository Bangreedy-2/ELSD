from typing import Any
from src.antlr_gen.GGCodeVisitor import GGCodeVisitor
from src.antlr_gen.GGCodeParser import GGCodeParser
from src.ast_nodes.program import Program
from src.ast_nodes.statements import (
    VariableDeclaration, Assignment, MoveStatement, IfStatement,
    RepeatStatement, Block, Statement, StopStatement, PauseStatement,
    TemperatureStatement, WaitStatement, UseStatement, SetStatement,
    DefineStatement, AddShapeStatement, WhileStatement, HomeStatement
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
        # return self.visit(ctx.getChild(0))
        child = ctx.getChild(0)
        # print(f"DEBUG: Visiting Statement -> {type(child)}")
        return self.visit(child)

    def visitMoveStatement(self, ctx: GGCodeParser.MoveStatementContext):
        target = self.visit(ctx.moveTarget())
        return MoveStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            x=Literal(line=0, column=0, value=0), # Dummy
            y=Literal(line=0, column=0, value=0), # Dummy
            target=target
        )

    def visitHomeStatement(self, ctx: GGCodeParser.HomeStatementContext):

        # homeStatement: HOME (axisList)?;
        # axisList: axis (axis)*;
        axes = []
        if ctx.axisList():
            # Iterate through axis children
            for i in range(ctx.axisList().getChildCount()):
                # axis: 'X' | 'Y' | 'Z' | 'E';
                axis_ctx = ctx.axisList().axis(i)
                if axis_ctx:
                    axes.append(axis_ctx.getText())
        return HomeStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            axes=axes
        )

    def visitMoveTarget(self, ctx: GGCodeParser.MoveTargetContext):
        return self.visit(ctx.getChild(0))

    def visitCoordinateTarget(self, ctx: GGCodeParser.CoordinateTargetContext):
        return self.visit(ctx.getChild(0))

    def visitAxisSingle(self, ctx: GGCodeParser.AxisSingleContext):
        val = ctx.AXIS_VALUE().getText()
        return {'type': 'axis_single', 'values': [val]}

    def visitAxisPair(self, ctx: GGCodeParser.AxisPairContext):
        val1 = ctx.AXIS_VALUE(0).getText()
        val2 = ctx.AXIS_VALUE(1).getText()
        return {'type': 'axis_pair', 'values': [val1, val2]}

    def visitAxisTriplet(self, ctx: GGCodeParser.AxisTripletContext):
        val1 = ctx.AXIS_VALUE(0).getText()
        val2 = ctx.AXIS_VALUE(1).getText()
        val3 = ctx.AXIS_VALUE(2).getText()
        return {'type': 'axis_triplet', 'values': [val1, val2, val3]}

    def visitPointTarget(self, ctx: GGCodeParser.PointTargetContext):
        return {'type': 'point', 'name': ctx.getText()}

    def visitNamedTarget(self, ctx: GGCodeParser.NamedTargetContext):
        return {'type': 'named', 'name': ctx.getText()}


    # Control Flow
    def visitConditionalStatement(self, ctx: GGCodeParser.ConditionalStatementContext):
        cond = self.visit(ctx.condition())
        blocks = ctx.blockStatement()
        then_branch = self.visit(blocks[0])
        else_branch = self.visit(blocks[1]) if len(blocks) > 1 else None
        return IfStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            condition=cond,
            then_branch=then_branch,
            else_branch=else_branch
        )

    def visitLoopStatement(self, ctx: GGCodeParser.LoopStatementContext):
        if ctx.REPEAT():
            count = self.visit(ctx.repeatCount())
            body = self.visit(ctx.blockStatement()) # Corrected context
            return RepeatStatement(
                line=ctx.start.line,
                column=ctx.start.column,
                count=count,
                body=body
            )
        elif ctx.WHILE():
            cond = self.visit(ctx.condition())
            body = self.visit(ctx.blockStatement())
            return WhileStatement(
                line=ctx.start.line,
                column=ctx.start.column,
                condition=cond,
                body=body
            )
        return None

    def visitBlockStatement(self, ctx: GGCodeParser.BlockStatementContext): # Renamed from visitBlock
        return self.visit(ctx.statementList())

    # Definition Commands
    def visitDefinitionStatement(self, ctx: GGCodeParser.DefinitionStatementContext):
        return self.visit(ctx.getChild(0))

    def visitDefineStatement(self, ctx: GGCodeParser.DefineStatementContext):
        return DefineStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            identifier=ctx.IDENTIFIER().getText(),
            location=self.visit(ctx.locationDefinition())
        )

    def visitLocationDefinition(self, ctx: GGCodeParser.LocationDefinitionContext):
        # returns whatever coordinatePair or pointTarget returns
        return self.visit(ctx.getChild(0))

    # Old variable handlers removed

    def visitSimpleStatement(self, ctx: GGCodeParser.SimpleStatementContext):
        return self.visit(ctx.getChild(0))

    # Expressions
    def visitUnaryExpression(self, ctx: GGCodeParser.UnaryExpressionContext):
        # unaryExpression -> MINUS unaryExpression | primaryExpression
        # Children could be MINUS and unaryExpression OR primaryExpression
        if ctx.MINUS():
            operand = self.visit(ctx.unaryExpression())
            return UnaryExpression(
                line=ctx.start.line,
                column=ctx.start.column,
                operator=TokenType.MINUS,
                operand=operand
            )
        return self.visit(ctx.primaryExpression())

    def visitMultiplicativeExpression(self, ctx: GGCodeParser.MultiplicativeExpressionContext):
        left = self.visit(ctx.unaryExpression())
        return self._processMultiplicativeTail(left, ctx.multiplicativeTail())

    def _processMultiplicativeTail(self, left, ctx):
        if not ctx or ctx.getChildCount() == 0:
            return left

        op_ctx = ctx.mulOperator()
        if not op_ctx: return left

        op_token = op_ctx.getChild(0).getSymbol()
        op_type = TokenType.STAR if op_token.type == GGCodeParser.STAR else TokenType.SLASH

        right = self.visit(ctx.unaryExpression())

        result = BinaryExpression(
            line=left.line,
            column=left.column,
            left=left,
            operator=op_type,
            right=right
        )

        return self._processMultiplicativeTail(result, ctx.multiplicativeTail())

    def visitAdditiveExpression(self, ctx: GGCodeParser.AdditiveExpressionContext):
        left = self.visit(ctx.multiplicativeExpression())
        return self._processAdditiveTail(left, ctx.additiveTail())

    def _processAdditiveTail(self, left, ctx):
        if not ctx or ctx.getChildCount() == 0:
            return left

        op_ctx = ctx.addOperator()
        if not op_ctx: return left

        op_token = op_ctx.getChild(0).getSymbol()
        op_type = TokenType.PLUS if op_token.type == GGCodeParser.PLUS else TokenType.MINUS

        right = self.visit(ctx.multiplicativeExpression())

        result = BinaryExpression(
            line=left.line,
            column=left.column,
            left=left,
            operator=op_type,
            right=right
        )

        return self._processAdditiveTail(result, ctx.additiveTail())

    def visitComparisonExpression(self, ctx: GGCodeParser.ComparisonExpressionContext):
        left = self.visit(ctx.additiveExpression())
        return self._processComparisonTail(left, ctx.comparisonTail())

    def _processComparisonTail(self, left, ctx):
        if not ctx or ctx.getChildCount() == 0:
            return left

        op_ctx = ctx.comparisonOperator()
        if not op_ctx: return left

        op_token = op_ctx.getChild(0).getSymbol()
        op_map = {
            GGCodeParser.GT: TokenType.GT,
            GGCodeParser.LT: TokenType.LT,
            GGCodeParser.GTE: TokenType.GTE,
            GGCodeParser.LTE: TokenType.LTE,
            GGCodeParser.EQ: TokenType.EQ,
            GGCodeParser.NEQ: TokenType.NEQ
        }
        op = op_map[op_token.type]

        right = self.visit(ctx.additiveExpression())

        result = BinaryExpression(
            line=left.line,
            column=left.column,
            left=left,
            operator=op,
            right=right
        )

        return self._processComparisonTail(result, ctx.comparisonTail())

    def visitPrimaryExpression(self, ctx: GGCodeParser.PrimaryExpressionContext):
        if ctx.numericValue():
            val = self.visit(ctx.numericValue())
            return Literal(line=ctx.start.line, column=ctx.start.column, value=val)
        elif ctx.IDENTIFIER():
            return Identifier(line=ctx.start.line, column=ctx.start.column, name=ctx.IDENTIFIER().getText())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None

    def visitGeometryStatement(self, ctx: GGCodeParser.GeometryStatementContext):
        return self.visit(ctx.getChild(0))

    def visitAddStatement(self, ctx: GGCodeParser.AddStatementContext):
        return self.visit(ctx.getChild(1)) # Child 0 is ADD, Child 1 is shapeStatement

    def visitShapeStatement(self, ctx: GGCodeParser.ShapeStatementContext):
        return self.visit(ctx.getChild(0))

    def visitSquareStatement(self, ctx: GGCodeParser.SquareStatementContext):
        # squareStatement: SQUARE squareParameters
        params = self.visit(ctx.squareParameters())
        return AddShapeStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            shape_type="square",
            params=params
        )

    def visitRectangleStatement(self, ctx: GGCodeParser.RectangleStatementContext):
        # rectangleStatement: RECTANGLE centerClause widthClause lengthClause
        center = self.visit(ctx.centerClause())
        width = self.visit(ctx.widthClause())
        length = self.visit(ctx.lengthClause())
        return AddShapeStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            shape_type="rectangle",
            params={**center, **width, **length}
        )

    def visitCircleStatement(self, ctx: GGCodeParser.CircleStatementContext):
        # circleStatement: CIRCLE centerClause radiusClause
        center = self.visit(ctx.centerClause())
        radius = self.visit(ctx.radiusClause())
        return AddShapeStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            shape_type="circle",
            params={**center, **radius}
        )

    def visitLineStatement(self, ctx: GGCodeParser.LineStatementContext):
        # lineStatement: LINE fromClause toClause
        start = self.visit(ctx.fromClause())
        end = self.visit(ctx.toClause())
        return AddShapeStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            shape_type="line",
            params={**start, **end}
        )

    def visitSquareParameters(self, ctx: GGCodeParser.SquareParametersContext):
        # centerClause lengthClause
        center = self.visit(ctx.centerClause())
        length = self.visit(ctx.lengthClause())
        return {**center, **length}

    def visitCenterClause(self, ctx: GGCodeParser.CenterClauseContext):
        return {"center": self.visit(ctx.coordinatePair())}

    def visitLengthClause(self, ctx: GGCodeParser.LengthClauseContext):
        return {"length": self.visit(ctx.numericValue())}

    def visitWidthClause(self, ctx: GGCodeParser.WidthClauseContext):
        return {"width": self.visit(ctx.numericValue())}

    def visitRadiusClause(self, ctx: GGCodeParser.RadiusClauseContext):
        return {"radius": self.visit(ctx.numericValue())}

    def visitFromClause(self, ctx: GGCodeParser.FromClauseContext):
        return {"from": self.visit(ctx.coordinatePair())}

    def visitToClause(self, ctx: GGCodeParser.ToClauseContext):
        return {"to": self.visit(ctx.coordinatePair())}

    def visitCoordinatePair(self, ctx: GGCodeParser.CoordinatePairContext):
        x = self.visit(ctx.numericValue(0))
        y = self.visit(ctx.numericValue(1))
        return [x, y] # List of Literals

    def visitNumericValue(self, ctx: GGCodeParser.NumericValueContext):
        if ctx.INTERGER():
            return int(ctx.INTERGER().getText())
        else:
            return float(ctx.DECIMAL().getText())

    def visitStatementList(self, ctx: GGCodeParser.StatementListContext):
        stmts = []
        current = ctx
        while current:
            stmt_ctx = current.statement()
            if not stmt_ctx:
                break

            res = self.visit(stmt_ctx)
            if res:
                stmts.append(res)

            if current.getChildCount() > 1:
                next_node = current.getChild(1)
                if isinstance(next_node, GGCodeParser.StatementListContext):
                    current = next_node
                else:
                    current = None
            else:
                current = None

        return Block(line=ctx.start.line, column=ctx.start.column, statements=stmts)

    def visitMachineStatement(self, ctx: GGCodeParser.MachineStatementContext):
        return self.visit(ctx.getChild(0))

    def visitTemperatureStatement(self, ctx: GGCodeParser.TemperatureStatementContext):
        val_text = ctx.temperatureValue().getText()
        # Parse 100C -> 100
        val = int(val_text[:-1])
        return TemperatureStatement(line=ctx.start.line, column=ctx.start.column, value=Literal(line=ctx.start.line, column=ctx.start.column, value=val))

    def visitWaitStatement(self, ctx: GGCodeParser.WaitStatementContext):
        dur_ctx = ctx.durationValue()
        val = int(dur_ctx.INTERGER().getText())
        unit = "seconds" if dur_ctx.SECONDS() else "minutes"
        return WaitStatement(line=ctx.start.line, column=ctx.start.column, duration=Literal(line=ctx.start.line, column=ctx.start.column, value=val), unit=unit)

    def visitUseStatement(self, ctx: GGCodeParser.UseStatementContext):
        return UseStatement(line=ctx.start.line, column=ctx.start.column, tool_name=ctx.IDENTIFIER().getText())

    def visitSetStatement(self, ctx: GGCodeParser.SetStatementContext):
        return SetStatement(
            line=ctx.start.line,
            column=ctx.start.column,
            identifier=ctx.IDENTIFIER().getText(),
            expression=self.visit(ctx.expression())
        )

    def visitCondition(self, ctx: GGCodeParser.ConditionContext):
        return self.visit(ctx.getChild(0))

    def visitRepeatCount(self, ctx: GGCodeParser.RepeatCountContext):
        if ctx.INTERGER():
            val = int(ctx.INTERGER().getText())
            return Literal(line=ctx.start.line, column=ctx.start.column, value=val)
        else:
            return Identifier(line=ctx.start.line, column=ctx.start.column, name=ctx.IDENTIFIER().getText())
