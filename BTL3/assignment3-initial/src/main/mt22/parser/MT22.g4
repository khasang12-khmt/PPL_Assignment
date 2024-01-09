grammar MT22;

@lexer::header {
# KHA SANG - 2010576
from lexererr import *
import re
}

options {
	language = Python3;
}

program: decl_list EOF;

// *****************************TYPES AND DECLARATIONS*****************************
decl_list: decl decl_list | decl;
decl: func | init_stmt;

atomic_type: BOOLEAN | INTEGER | FLOAT | STRING;
int_list: (INT_LIT | ZERO_LIT) COMMA int_list
	| (INT_LIT | ZERO_LIT);
array_type: ARRAY LSB int_list RSB OF atomic_type;
void_type: VOID;
auto_type: AUTO;
vtype: atomic_type | array_type | void_type | auto_type;

// Variables
variable:
	id_list ':' vtype (
		ASM value_list_stmt[$id_list.count] (
			{$value_list_stmt.count_diff == 0}?
		)
		|
	);
id_list
	returns[count = 0]:
	IDENTIFIER {$count+=1} (COMMA IDENTIFIER {$count+=1})*;
value_list_stmt[count]
	returns[count_diff]:
	expr {$count-=1} ({$count > 0}? COMMA expr {$count-=1})* {$count_diff = $count};

param: (INHERIT |) (OUT |) IDENTIFIER ':' vtype;
array_lit: LP (expr_list |) RP;
param_list: param COMMA param_list | param;
scalar_variable: IDENTIFIER (idx_ops |);

// Functions
func:
	IDENTIFIER ':' FUNCTION vtype LB (param_list |) RB (
		INHERIT IDENTIFIER
		|
	) block_stmt;
// *****************************END TYPES AND DECLARATIONS*****************************

// *****************************EXPRESSIONS***************************** Precedence
expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 rel_ops expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: IDENTIFIER idx_ops | LB expr RB | operands;
expr_list: expr COMMA expr_list | expr;

const:
	ZERO_LIT
	| INT_LIT
	| FLOAT_LIT
	| STRING_LIT
	| bool_lit
	| array_lit;
bool_lit: TRUE | FALSE;
//arith_ops: ADD | SUB | MUL | DIV | MOD;
//bool_ops: NOT | AND | OR;
//str_ops: CONCAT;
rel_ops: EQ | NEQ | GT | GTE | LT | LTE;
idx_ops: LSB expr_list RSB;
call_expr: IDENTIFIER LB (expr_list |) RB;
operands:
	const
	| variable
	| LB expr RB
	| call_expr
	| IDENTIFIER;
// *****************************END EXPRESSIONS*****************************

// *****************************STATEMENTS*****************************
stmt:
	asm_stmt SEMICOLON
	| if_stmt
	| for_stmt
	| while_stmt
	| dowhile_stmt
	| break_stmt
	| continue_stmt
	| call_stmt
	| return_stmt
	| block_stmt;
stmt_list: (stmt | init_stmt) stmt_list |;
init_stmt: variable SEMICOLON;
asm_stmt: scalar_variable ASM expr;
if_stmt: IF LB expr RB stmt (ELSE stmt |);
for_stmt:
	FOR LB asm_stmt COMMA expr COMMA expr RB stmt;
while_stmt: WHILE LB expr RB stmt;
dowhile_stmt: DO block_stmt WHILE LB expr RB SEMICOLON;
break_stmt: BREAK SEMICOLON;
continue_stmt: CONTINUE SEMICOLON;
return_stmt: RETURN (expr |) SEMICOLON;
call_stmt: IDENTIFIER LB (expr_list |) RB SEMICOLON;
block_stmt: LP stmt_list RP;
// *****************************END STATEMENTS*****************************

// *****************************COMMENTS*****************************
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
// *****************************END COMMENTS*****************************

// *****************************KEYWORDS*****************************
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
ARRAY: 'array';
INHERIT: 'inherit';
// *****************************END KEYWORDS*****************************

// *****************************OPERATORS*****************************
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

NOT: '!';
AND: '&&';
OR: '||';

EQ: '==';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

CONCAT: '::';
// *****************************END OPERATORS*****************************

// *****************************SEPERATORS*****************************
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LP: '{';
RP: '}';
ASM: '=';
// *****************************END SEPERATORS*****************************

// *****************************LITERALS*****************************

FLOAT_LIT:
	(
		(ZERO_LIT | INT_LIT) DEC_PART (EXP_PART |)
		| (ZERO_LIT | INT_LIT) EXP_PART
		| DEC_PART EXP_PART
	) {self.text = re.sub('_','',self.text)};

ZERO_LIT: '0';

INT_LIT: INT_PART {self.text = re.sub('_','',self.text)};

BOOL_LIT: TRUE | FALSE;

// "Hello\\b": ok, "Hello\\k": illegal, "Hello\n": Unclose, "Hello\t": ok, "Hello\k":ok
STRING_LIT: '"' CHAR* '"' {self.text = self.text[1:-1]};
fragment VALID_ESC: '\\' [btnfr'\\"];
// \", \b, \t, \f, \r,\',\"
fragment CHAR: VALID_ESC | ~[\r\n"];
// VALID_ESC (\\b,..) and non-esc chars (-\b,\t,\n,\f,\r,\\,") and no (valid) double quotes
fragment INVALID_ESC: ('\\' ~[btnfr'"\\]);
// illegal esc: \\e,\\o,\\t

// *****************************END LITERALS*****************************

WS: [ \b\t\r\n\f]+ -> skip;
// skip spaces, tabs, newlines
IDENTIFIER: (UNDERSCORE | LETTER) (LETTER | UNDERSCORE | DIGIT)*;

fragment DEC_PART: '.' DIGIT*;
fragment EXP_PART: [eE] [+-]? DIGIT+;
INT_PART: [1-9]('_'? DIGIT)*;
// recognizable, to avoid warnings
fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';

UNCLOSE_STRING:
	'"' CHAR* ([\n\r] | EOF) {
    ESC = ['\r', '\n']
    text = str(self.text)
    raise UncloseString(text[1:]) 
};

ILLEGAL_ESCAPE:
	'"' CHAR* INVALID_ESC {
	illegal_str_from_beginning = str(self.text)
	raise IllegalEscape(illegal_str_from_beginning[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};