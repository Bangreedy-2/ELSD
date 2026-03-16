grammar GGCode;

// Program Structure
program: statementList EOF;

statementList: statement statementList | statement;

statement
    : simpleStatement
    | compoundStatement
    ;

simpleStatement
    : motionStatement
    | machineStatement
    | geometryStatement
    | definitionStatement
    ;

compoundStatement
    : conditionalStatement
    | loopStatement
    | blockStatement
    ;

// Motion Commands
motionStatement
    : moveStatement
    | stopStatement
    | pauseStatement
    | homeStatement
    ;

moveStatement: MOVE TO moveTarget;

homeStatement: HOME (axisList)?;

axisList: axis (axis)*;
axis: 'X' | 'Y' | 'Z' | 'E';

moveTarget
    : coordinateTarget
    | pointTarget
    | namedTarget
    ;

coordinateTarget
    : axisSingle
    | axisPair
    | axisTriplet
    | measurePair
    | measureTriplet
    ;

axisSingle: AXIS_VALUE;
axisPair: AXIS_VALUE AXIS_VALUE;
axisTriplet: AXIS_VALUE AXIS_VALUE AXIS_VALUE;
measurePair: measure measure;
measureTriplet: measure measure measure;

pointTarget: BASE | CENTER_POINT | ORIGIN;
namedTarget: IDENTIFIER;

stopStatement: STOP AT measure;
pauseStatement: PAUSE AT LAYER INTERGER;

// Machine Control Commands
machineStatement
    : temperatureStatement
    | waitStatement
    | useStatement
    ;

temperatureStatement: TEMPERATURE temperatureValue;
waitStatement: WAIT FOR durationValue;
useStatement: USE IDENTIFIER;

durationValue
    : INTERGER SECONDS
    | INTERGER MINUTES
    ;

temperatureValue: TEMPERATURE_VALUE;

// Geometry Commands
geometryStatement: addStatement;
addStatement: ADD shapeStatement;

shapeStatement
    : squareStatement
    | rectangleStatement
    | circleStatement
    | lineStatement
    ;

squareStatement: SQUARE squareParameters;
squareParameters: centerClause lengthClause;

rectangleStatement: RECTANGLE centerClause widthClause lengthClause;

circleStatement: CIRCLE centerClause radiusClause;

lineStatement: LINE fromClause toClause;

centerClause: CENTER coordinatePair;
widthClause: WIDTH numericValue;
lengthClause: LENGTH numericValue;
radiusClause: RADIUS numericValue;
fromClause: FROM coordinatePair;
toClause: TO coordinatePair;

coordinatePair: numericValue numericValue;

// Definition Commands
definitionStatement
    : defineStatement
    | setStatement
    ;

defineStatement: DEFINE IDENTIFIER AS locationDefinition;
locationDefinition
    : coordinatePair
    | pointTarget
    ;

setStatement: SET IDENTIFIER TO expression;

// Control Flow
conditionalStatement: IF condition THEN blockStatement (ELSE blockStatement)?;
loopStatement
    : REPEAT repeatCount TIMES blockStatement
    | WHILE condition blockStatement
    ;

repeatCount: INTERGER | IDENTIFIER;
blockStatement: LBRACE statementList RBRACE;

// Expressions
condition: expression;

expression: comparisonExpression;

comparisonExpression: additiveExpression comparisonTail;
comparisonTail: comparisonOperator additiveExpression comparisonTail | ;

additiveExpression: multiplicativeExpression additiveTail;
additiveTail: addOperator multiplicativeExpression additiveTail | ;

multiplicativeExpression: unaryExpression multiplicativeTail;
multiplicativeTail: mulOperator unaryExpression multiplicativeTail | ;

unaryExpression: MINUS unaryExpression | primaryExpression;

primaryExpression
    : numericValue
    | IDENTIFIER
    | LPAREN expression RPAREN
    ;

comparisonOperator: EQ | NEQ | LT | LTE | GT | GTE;
addOperator: PLUS | MINUS;
mulOperator: STAR | SLASH;

numericValue: INTERGER | DECIMAL;
measure: MEASURE;

// Lexer Rules

// Keywords
STOP: [Ss][Tt][Oo][Pp];
PAUSE: [Pp][Aa][Uu][Ss][Ee];
AT: [Aa][Tt];
LAYER: [Ll][Aa][Yy][Ee][Rr];
TEMPERATURE: [Tt][Ee][Mm][Pp][Ee][Rr][Aa][Tt][Uu][Rr][Ee];
MOVE: [Mm][Oo][Vv][Ee];
TO: [Tt][Oo];
ADD: [Aa][Dd][Dd];
SQUARE: [Ss][Qq][Uu][Aa][Rr][Ee];
CENTER: [Cc][Ee][Nn][Tt][Ee][Rr];
LENGTH: [Ll][Ee][Nn][Gg][Tt][Hh];
WIDTH: [Ww][Ii][Dd][Tt][Hh];
RECTANGLE: [Rr][Ee][Cc][Tt][Aa][Nn][Gg][Ll][Ee];
CIRCLE: [Cc][Ii][Rr][Cc][Ll][Ee];
RADIUS: [Rr][Aa][Dd][Ii][Uu][Ss];
LINE: [Ll][Ii][Nn][Ee];
FROM: [Ff][Rr][Oo][Mm];
BASE: [Bb][Aa][Ss][Ee];
CENTER_POINT: [Cc][Ee][Nn][Tt][Ee][Rr] '_' [Pp][Oo][Ii][Nn][Tt]; // Disambiguate from CENTER keyword?
ORIGIN: [Oo][Rr][Ii][Gg][Ii][Nn];
SET: [Ss][Ee][Tt];
DEFINE: [Dd][Ee][Ff][Ii][Nn][Ee];
AS: [Aa][Ss];
REPEAT: [Rr][Ee][Pp][Ee][Aa][Tt];
TIMES: [Tt][Ii][Mm][Ee][Ss];
IF: [Ii][Ff];
THEN: [Tt][Hh][Ee][Nn];
ELSE: [Ee][Ll][Ss][Ee];
WHILE: [Ww][Hh][Ii][Ll][Ee];
WAIT: [Ww][Aa][Ii][Tt];
FOR: [Ff][Oo][Rr];
SECONDS: [Ss][Ee][Cc][Oo][Nn][Dd][Ss];
MINUTES: [Mm][Ii][Nn][Uu][Tt][Ee][Ss];
USE: [Uu][Ss][Ee];
HOME: [Hh][Oo][Mm][Ee];

KEY_X: [Xx];
KEY_Y: [Yy];
KEY_Z: [Zz];
KEY_E: [Ee];

// Delimiters & Operators
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GTE: '>=';
LTE: '<=';

// Complex Tokens
// Measure: 20mm, 2.5cm
MEASURE: [0-9]+ ('.' [0-9]+)? ('mm' | 'cm');

// Temperature: 100C, 250c
TEMPERATURE_VALUE: [0-9]+ [Cc];

// Axis Value: X25, Y-10.5, Z0
AXIS_VALUE: [XYZxyzEe] '-'? [0-9]+ ('.' [0-9]+)?;

// Identifier: standard variable names
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Numeric
INTERGER: [0-9]+;
DECIMAL: [0-9]+ '.' [0-9]+;

// Whitespace and Comments
WS: [ \t\r\n]+ -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
