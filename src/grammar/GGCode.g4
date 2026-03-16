grammar GGCode;

// Parser Rules
program: statement* EOF;

statement
    : variableDeclaration
    | assignment
    | moveStatement
    | ifStatement
    | repeatStatement
    | block
    ;

variableDeclaration: LET IDENTIFIER ASSIGN expression SEMI;
assignment: IDENTIFIER ASSIGN expression SEMI;
moveStatement: MOVE LPAREN expression COMMA expression RPAREN SEMI;
ifStatement: IF LPAREN expression RPAREN block (ELSE block)?;
repeatStatement: REPEAT LPAREN expression RPAREN block;
block: LBRACE statement* RBRACE;

expression
    : MINUS expression                           # unaryExpression
    | expression (STAR | SLASH) expression       # multiplicativeExpression
    | expression (PLUS | MINUS) expression       # additiveExpression
    | expression (GT | LT | GTE | LTE) expression # relationalExpression
    | expression (EQ | NEQ) expression           # equalityExpression
    | primary                                    # primaryExpression
    ;

primary
    : NUMBER
    | BOOLEAN
    | IDENTIFIER
    | LPAREN expression RPAREN
    ;

// Lexer Rules
LET: 'let';
MOVE: 'move';
IF: 'if';
ELSE: 'else';
REPEAT: 'repeat';
TRUE: 'true';
FALSE: 'false';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
SEMI: ';';
ASSIGN: '=';

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

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
BOOLEAN: TRUE | FALSE;

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;


