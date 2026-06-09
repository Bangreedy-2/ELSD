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


    # Visit a parse tree produced by GGCodeParser#statementList.
    def visitStatementList(self, ctx:GGCodeParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#statement.
    def visitStatement(self, ctx:GGCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#simpleStatement.
    def visitSimpleStatement(self, ctx:GGCodeParser.SimpleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#compoundStatement.
    def visitCompoundStatement(self, ctx:GGCodeParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#motionStatement.
    def visitMotionStatement(self, ctx:GGCodeParser.MotionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#moveStatement.
    def visitMoveStatement(self, ctx:GGCodeParser.MoveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#homeStatement.
    def visitHomeStatement(self, ctx:GGCodeParser.HomeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#axisList.
    def visitAxisList(self, ctx:GGCodeParser.AxisListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#axis.
    def visitAxis(self, ctx:GGCodeParser.AxisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#moveTarget.
    def visitMoveTarget(self, ctx:GGCodeParser.MoveTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#coordinateTarget.
    def visitCoordinateTarget(self, ctx:GGCodeParser.CoordinateTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#axisSingle.
    def visitAxisSingle(self, ctx:GGCodeParser.AxisSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#axisPair.
    def visitAxisPair(self, ctx:GGCodeParser.AxisPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#axisTriplet.
    def visitAxisTriplet(self, ctx:GGCodeParser.AxisTripletContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#measurePair.
    def visitMeasurePair(self, ctx:GGCodeParser.MeasurePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#measureTriplet.
    def visitMeasureTriplet(self, ctx:GGCodeParser.MeasureTripletContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#pointTarget.
    def visitPointTarget(self, ctx:GGCodeParser.PointTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#namedTarget.
    def visitNamedTarget(self, ctx:GGCodeParser.NamedTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#stopStatement.
    def visitStopStatement(self, ctx:GGCodeParser.StopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#pauseStatement.
    def visitPauseStatement(self, ctx:GGCodeParser.PauseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#layerAnchor.
    def visitLayerAnchor(self, ctx:GGCodeParser.LayerAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#heightAnchor.
    def visitHeightAnchor(self, ctx:GGCodeParser.HeightAnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#atBlockStatement.
    def visitAtBlockStatement(self, ctx:GGCodeParser.AtBlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#machineStatement.
    def visitMachineStatement(self, ctx:GGCodeParser.MachineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#temperatureStatement.
    def visitTemperatureStatement(self, ctx:GGCodeParser.TemperatureStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#waitStatement.
    def visitWaitStatement(self, ctx:GGCodeParser.WaitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#useStatement.
    def visitUseStatement(self, ctx:GGCodeParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#durationValue.
    def visitDurationValue(self, ctx:GGCodeParser.DurationValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#temperatureValue.
    def visitTemperatureValue(self, ctx:GGCodeParser.TemperatureValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#geometryStatement.
    def visitGeometryStatement(self, ctx:GGCodeParser.GeometryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#addStatement.
    def visitAddStatement(self, ctx:GGCodeParser.AddStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#shapeStatement.
    def visitShapeStatement(self, ctx:GGCodeParser.ShapeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#squareStatement.
    def visitSquareStatement(self, ctx:GGCodeParser.SquareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#squareParameters.
    def visitSquareParameters(self, ctx:GGCodeParser.SquareParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#rectangleStatement.
    def visitRectangleStatement(self, ctx:GGCodeParser.RectangleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#circleStatement.
    def visitCircleStatement(self, ctx:GGCodeParser.CircleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#lineStatement.
    def visitLineStatement(self, ctx:GGCodeParser.LineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#centerClause.
    def visitCenterClause(self, ctx:GGCodeParser.CenterClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#widthClause.
    def visitWidthClause(self, ctx:GGCodeParser.WidthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#lengthClause.
    def visitLengthClause(self, ctx:GGCodeParser.LengthClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#radiusClause.
    def visitRadiusClause(self, ctx:GGCodeParser.RadiusClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#fromClause.
    def visitFromClause(self, ctx:GGCodeParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#toClause.
    def visitToClause(self, ctx:GGCodeParser.ToClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#coordinatePair.
    def visitCoordinatePair(self, ctx:GGCodeParser.CoordinatePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#definitionStatement.
    def visitDefinitionStatement(self, ctx:GGCodeParser.DefinitionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#defineStatement.
    def visitDefineStatement(self, ctx:GGCodeParser.DefineStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#locationDefinition.
    def visitLocationDefinition(self, ctx:GGCodeParser.LocationDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#setStatement.
    def visitSetStatement(self, ctx:GGCodeParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#conditionalStatement.
    def visitConditionalStatement(self, ctx:GGCodeParser.ConditionalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#loopStatement.
    def visitLoopStatement(self, ctx:GGCodeParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#repeatCount.
    def visitRepeatCount(self, ctx:GGCodeParser.RepeatCountContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#blockStatement.
    def visitBlockStatement(self, ctx:GGCodeParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#condition.
    def visitCondition(self, ctx:GGCodeParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#expression.
    def visitExpression(self, ctx:GGCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:GGCodeParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#comparisonTail.
    def visitComparisonTail(self, ctx:GGCodeParser.ComparisonTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:GGCodeParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#additiveTail.
    def visitAdditiveTail(self, ctx:GGCodeParser.AdditiveTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:GGCodeParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#multiplicativeTail.
    def visitMultiplicativeTail(self, ctx:GGCodeParser.MultiplicativeTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#unaryExpression.
    def visitUnaryExpression(self, ctx:GGCodeParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:GGCodeParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:GGCodeParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#addOperator.
    def visitAddOperator(self, ctx:GGCodeParser.AddOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#mulOperator.
    def visitMulOperator(self, ctx:GGCodeParser.MulOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#numericValue.
    def visitNumericValue(self, ctx:GGCodeParser.NumericValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GGCodeParser#measure.
    def visitMeasure(self, ctx:GGCodeParser.MeasureContext):
        return self.visitChildren(ctx)



del GGCodeParser