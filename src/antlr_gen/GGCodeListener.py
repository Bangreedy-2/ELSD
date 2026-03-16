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


    # Enter a parse tree produced by GGCodeParser#statementList.
    def enterStatementList(self, ctx:GGCodeParser.StatementListContext):
        pass

    # Exit a parse tree produced by GGCodeParser#statementList.
    def exitStatementList(self, ctx:GGCodeParser.StatementListContext):
        pass


    # Enter a parse tree produced by GGCodeParser#statement.
    def enterStatement(self, ctx:GGCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#statement.
    def exitStatement(self, ctx:GGCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#simpleStatement.
    def enterSimpleStatement(self, ctx:GGCodeParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#simpleStatement.
    def exitSimpleStatement(self, ctx:GGCodeParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#compoundStatement.
    def enterCompoundStatement(self, ctx:GGCodeParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#compoundStatement.
    def exitCompoundStatement(self, ctx:GGCodeParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#motionStatement.
    def enterMotionStatement(self, ctx:GGCodeParser.MotionStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#motionStatement.
    def exitMotionStatement(self, ctx:GGCodeParser.MotionStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#moveStatement.
    def enterMoveStatement(self, ctx:GGCodeParser.MoveStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#moveStatement.
    def exitMoveStatement(self, ctx:GGCodeParser.MoveStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#moveTarget.
    def enterMoveTarget(self, ctx:GGCodeParser.MoveTargetContext):
        pass

    # Exit a parse tree produced by GGCodeParser#moveTarget.
    def exitMoveTarget(self, ctx:GGCodeParser.MoveTargetContext):
        pass


    # Enter a parse tree produced by GGCodeParser#coordinateTarget.
    def enterCoordinateTarget(self, ctx:GGCodeParser.CoordinateTargetContext):
        pass

    # Exit a parse tree produced by GGCodeParser#coordinateTarget.
    def exitCoordinateTarget(self, ctx:GGCodeParser.CoordinateTargetContext):
        pass


    # Enter a parse tree produced by GGCodeParser#axisPair.
    def enterAxisPair(self, ctx:GGCodeParser.AxisPairContext):
        pass

    # Exit a parse tree produced by GGCodeParser#axisPair.
    def exitAxisPair(self, ctx:GGCodeParser.AxisPairContext):
        pass


    # Enter a parse tree produced by GGCodeParser#axisTriplet.
    def enterAxisTriplet(self, ctx:GGCodeParser.AxisTripletContext):
        pass

    # Exit a parse tree produced by GGCodeParser#axisTriplet.
    def exitAxisTriplet(self, ctx:GGCodeParser.AxisTripletContext):
        pass


    # Enter a parse tree produced by GGCodeParser#measurePair.
    def enterMeasurePair(self, ctx:GGCodeParser.MeasurePairContext):
        pass

    # Exit a parse tree produced by GGCodeParser#measurePair.
    def exitMeasurePair(self, ctx:GGCodeParser.MeasurePairContext):
        pass


    # Enter a parse tree produced by GGCodeParser#measureTriplet.
    def enterMeasureTriplet(self, ctx:GGCodeParser.MeasureTripletContext):
        pass

    # Exit a parse tree produced by GGCodeParser#measureTriplet.
    def exitMeasureTriplet(self, ctx:GGCodeParser.MeasureTripletContext):
        pass


    # Enter a parse tree produced by GGCodeParser#pointTarget.
    def enterPointTarget(self, ctx:GGCodeParser.PointTargetContext):
        pass

    # Exit a parse tree produced by GGCodeParser#pointTarget.
    def exitPointTarget(self, ctx:GGCodeParser.PointTargetContext):
        pass


    # Enter a parse tree produced by GGCodeParser#namedTarget.
    def enterNamedTarget(self, ctx:GGCodeParser.NamedTargetContext):
        pass

    # Exit a parse tree produced by GGCodeParser#namedTarget.
    def exitNamedTarget(self, ctx:GGCodeParser.NamedTargetContext):
        pass


    # Enter a parse tree produced by GGCodeParser#stopStatement.
    def enterStopStatement(self, ctx:GGCodeParser.StopStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#stopStatement.
    def exitStopStatement(self, ctx:GGCodeParser.StopStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#pauseStatement.
    def enterPauseStatement(self, ctx:GGCodeParser.PauseStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#pauseStatement.
    def exitPauseStatement(self, ctx:GGCodeParser.PauseStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#machineStatement.
    def enterMachineStatement(self, ctx:GGCodeParser.MachineStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#machineStatement.
    def exitMachineStatement(self, ctx:GGCodeParser.MachineStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#temperatureStatement.
    def enterTemperatureStatement(self, ctx:GGCodeParser.TemperatureStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#temperatureStatement.
    def exitTemperatureStatement(self, ctx:GGCodeParser.TemperatureStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#waitStatement.
    def enterWaitStatement(self, ctx:GGCodeParser.WaitStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#waitStatement.
    def exitWaitStatement(self, ctx:GGCodeParser.WaitStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#useStatement.
    def enterUseStatement(self, ctx:GGCodeParser.UseStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#useStatement.
    def exitUseStatement(self, ctx:GGCodeParser.UseStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#durationValue.
    def enterDurationValue(self, ctx:GGCodeParser.DurationValueContext):
        pass

    # Exit a parse tree produced by GGCodeParser#durationValue.
    def exitDurationValue(self, ctx:GGCodeParser.DurationValueContext):
        pass


    # Enter a parse tree produced by GGCodeParser#temperatureValue.
    def enterTemperatureValue(self, ctx:GGCodeParser.TemperatureValueContext):
        pass

    # Exit a parse tree produced by GGCodeParser#temperatureValue.
    def exitTemperatureValue(self, ctx:GGCodeParser.TemperatureValueContext):
        pass


    # Enter a parse tree produced by GGCodeParser#geometryStatement.
    def enterGeometryStatement(self, ctx:GGCodeParser.GeometryStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#geometryStatement.
    def exitGeometryStatement(self, ctx:GGCodeParser.GeometryStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#addStatement.
    def enterAddStatement(self, ctx:GGCodeParser.AddStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#addStatement.
    def exitAddStatement(self, ctx:GGCodeParser.AddStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#shapeStatement.
    def enterShapeStatement(self, ctx:GGCodeParser.ShapeStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#shapeStatement.
    def exitShapeStatement(self, ctx:GGCodeParser.ShapeStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#squareStatement.
    def enterSquareStatement(self, ctx:GGCodeParser.SquareStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#squareStatement.
    def exitSquareStatement(self, ctx:GGCodeParser.SquareStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#squareParameters.
    def enterSquareParameters(self, ctx:GGCodeParser.SquareParametersContext):
        pass

    # Exit a parse tree produced by GGCodeParser#squareParameters.
    def exitSquareParameters(self, ctx:GGCodeParser.SquareParametersContext):
        pass


    # Enter a parse tree produced by GGCodeParser#rectangleStatement.
    def enterRectangleStatement(self, ctx:GGCodeParser.RectangleStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#rectangleStatement.
    def exitRectangleStatement(self, ctx:GGCodeParser.RectangleStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#circleStatement.
    def enterCircleStatement(self, ctx:GGCodeParser.CircleStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#circleStatement.
    def exitCircleStatement(self, ctx:GGCodeParser.CircleStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#lineStatement.
    def enterLineStatement(self, ctx:GGCodeParser.LineStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#lineStatement.
    def exitLineStatement(self, ctx:GGCodeParser.LineStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#centerClause.
    def enterCenterClause(self, ctx:GGCodeParser.CenterClauseContext):
        pass

    # Exit a parse tree produced by GGCodeParser#centerClause.
    def exitCenterClause(self, ctx:GGCodeParser.CenterClauseContext):
        pass


    # Enter a parse tree produced by GGCodeParser#widthClause.
    def enterWidthClause(self, ctx:GGCodeParser.WidthClauseContext):
        pass

    # Exit a parse tree produced by GGCodeParser#widthClause.
    def exitWidthClause(self, ctx:GGCodeParser.WidthClauseContext):
        pass


    # Enter a parse tree produced by GGCodeParser#lengthClause.
    def enterLengthClause(self, ctx:GGCodeParser.LengthClauseContext):
        pass

    # Exit a parse tree produced by GGCodeParser#lengthClause.
    def exitLengthClause(self, ctx:GGCodeParser.LengthClauseContext):
        pass


    # Enter a parse tree produced by GGCodeParser#radiusClause.
    def enterRadiusClause(self, ctx:GGCodeParser.RadiusClauseContext):
        pass

    # Exit a parse tree produced by GGCodeParser#radiusClause.
    def exitRadiusClause(self, ctx:GGCodeParser.RadiusClauseContext):
        pass


    # Enter a parse tree produced by GGCodeParser#fromClause.
    def enterFromClause(self, ctx:GGCodeParser.FromClauseContext):
        pass

    # Exit a parse tree produced by GGCodeParser#fromClause.
    def exitFromClause(self, ctx:GGCodeParser.FromClauseContext):
        pass


    # Enter a parse tree produced by GGCodeParser#toClause.
    def enterToClause(self, ctx:GGCodeParser.ToClauseContext):
        pass

    # Exit a parse tree produced by GGCodeParser#toClause.
    def exitToClause(self, ctx:GGCodeParser.ToClauseContext):
        pass


    # Enter a parse tree produced by GGCodeParser#coordinatePair.
    def enterCoordinatePair(self, ctx:GGCodeParser.CoordinatePairContext):
        pass

    # Exit a parse tree produced by GGCodeParser#coordinatePair.
    def exitCoordinatePair(self, ctx:GGCodeParser.CoordinatePairContext):
        pass


    # Enter a parse tree produced by GGCodeParser#definitionStatement.
    def enterDefinitionStatement(self, ctx:GGCodeParser.DefinitionStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#definitionStatement.
    def exitDefinitionStatement(self, ctx:GGCodeParser.DefinitionStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#defineStatement.
    def enterDefineStatement(self, ctx:GGCodeParser.DefineStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#defineStatement.
    def exitDefineStatement(self, ctx:GGCodeParser.DefineStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#locationDefinition.
    def enterLocationDefinition(self, ctx:GGCodeParser.LocationDefinitionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#locationDefinition.
    def exitLocationDefinition(self, ctx:GGCodeParser.LocationDefinitionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#setStatement.
    def enterSetStatement(self, ctx:GGCodeParser.SetStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#setStatement.
    def exitSetStatement(self, ctx:GGCodeParser.SetStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:GGCodeParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:GGCodeParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#loopStatement.
    def enterLoopStatement(self, ctx:GGCodeParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#loopStatement.
    def exitLoopStatement(self, ctx:GGCodeParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#repeatCount.
    def enterRepeatCount(self, ctx:GGCodeParser.RepeatCountContext):
        pass

    # Exit a parse tree produced by GGCodeParser#repeatCount.
    def exitRepeatCount(self, ctx:GGCodeParser.RepeatCountContext):
        pass


    # Enter a parse tree produced by GGCodeParser#blockStatement.
    def enterBlockStatement(self, ctx:GGCodeParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by GGCodeParser#blockStatement.
    def exitBlockStatement(self, ctx:GGCodeParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by GGCodeParser#condition.
    def enterCondition(self, ctx:GGCodeParser.ConditionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#condition.
    def exitCondition(self, ctx:GGCodeParser.ConditionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#expression.
    def enterExpression(self, ctx:GGCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#expression.
    def exitExpression(self, ctx:GGCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:GGCodeParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:GGCodeParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#comparisonTail.
    def enterComparisonTail(self, ctx:GGCodeParser.ComparisonTailContext):
        pass

    # Exit a parse tree produced by GGCodeParser#comparisonTail.
    def exitComparisonTail(self, ctx:GGCodeParser.ComparisonTailContext):
        pass


    # Enter a parse tree produced by GGCodeParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:GGCodeParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:GGCodeParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#additiveTail.
    def enterAdditiveTail(self, ctx:GGCodeParser.AdditiveTailContext):
        pass

    # Exit a parse tree produced by GGCodeParser#additiveTail.
    def exitAdditiveTail(self, ctx:GGCodeParser.AdditiveTailContext):
        pass


    # Enter a parse tree produced by GGCodeParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:GGCodeParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:GGCodeParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#multiplicativeTail.
    def enterMultiplicativeTail(self, ctx:GGCodeParser.MultiplicativeTailContext):
        pass

    # Exit a parse tree produced by GGCodeParser#multiplicativeTail.
    def exitMultiplicativeTail(self, ctx:GGCodeParser.MultiplicativeTailContext):
        pass


    # Enter a parse tree produced by GGCodeParser#unaryExpression.
    def enterUnaryExpression(self, ctx:GGCodeParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#unaryExpression.
    def exitUnaryExpression(self, ctx:GGCodeParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:GGCodeParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by GGCodeParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:GGCodeParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by GGCodeParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:GGCodeParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by GGCodeParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:GGCodeParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by GGCodeParser#addOperator.
    def enterAddOperator(self, ctx:GGCodeParser.AddOperatorContext):
        pass

    # Exit a parse tree produced by GGCodeParser#addOperator.
    def exitAddOperator(self, ctx:GGCodeParser.AddOperatorContext):
        pass


    # Enter a parse tree produced by GGCodeParser#mulOperator.
    def enterMulOperator(self, ctx:GGCodeParser.MulOperatorContext):
        pass

    # Exit a parse tree produced by GGCodeParser#mulOperator.
    def exitMulOperator(self, ctx:GGCodeParser.MulOperatorContext):
        pass


    # Enter a parse tree produced by GGCodeParser#numericValue.
    def enterNumericValue(self, ctx:GGCodeParser.NumericValueContext):
        pass

    # Exit a parse tree produced by GGCodeParser#numericValue.
    def exitNumericValue(self, ctx:GGCodeParser.NumericValueContext):
        pass


    # Enter a parse tree produced by GGCodeParser#measure.
    def enterMeasure(self, ctx:GGCodeParser.MeasureContext):
        pass

    # Exit a parse tree produced by GGCodeParser#measure.
    def exitMeasure(self, ctx:GGCodeParser.MeasureContext):
        pass



del GGCodeParser