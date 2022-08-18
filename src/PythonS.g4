grammar PythonS;

prog: decVars* decFunc* blocoMain
    ;

decVars: type (listaIds | listaAtribs)';'
    ;
    
type: 'int'
    | 'real'
    | 'string'
    | 'boolean'
    | 'void'
    ;

listaIds : ID(',' ID)*
    ;
listaAtribs:  ID '=' (ID|NUM|STRING) // todo: Add BoolExpr
    ;
decFunc: ('def' ID '(' listaParams* ')' type '{' decVars* decFunc* stmt+ '}')+
    ; // todo: Remove decFunc rule
blocoMain: 'def' 'main' '(' ')' '{' stmt+  '}'
    ;
stmt: for
    | doWhile ';'
    | if
    | atrib ';'
    | nativeFunc
    | ID ID operacao ID '(' expr ')' ';'
    | ID (NUM | ID) ';'
    | ID'(' ID expr ')' ';'
;
//todo: add func_call rule to statement or attribution
breakStmt: stmt
    | 'break'';'
;
atrib: ID '=' expr;
for: 'for' ID 'in' 'range' '(' range ')' '{' breakStmt '}'
;
doWhile: 'do' '{' breakStmt '}' 'while' '(' expr ')'
    ;
if: 'if' '(' expr ')' '{' stmt+ '}' ('else' '{' stmt+ '}')?
;

expr: e1= expr operacao term ';'
    |  term
    ;
term: t1=term operacao factor
    | factor            
    ;
// todo: fix precedence order / operations
factor: '(' expr ')' (';')?
    | (ID | NUM)
    ;
// todo: treat string variables

range:
NUM ':' NUM (':' NUM)?
;
listaParams: type ID | type ID ',' listaParams
  ;
nativeFunc: ID operacao 'input' '(' ')' ';'
          | print';'
          ;
print: 'print' '(' (NUM| ID)+ ')'
       |'print' '(' STRING ',' (NUM | ID) operacao (NUM| ID) ')'
       | 'print' '(' STRING ',' (NUM | ID) ')'
       |'print' '(' STRING  ','  STRING ')'
       |'print' '(' STRING ')'
       ;
// todo: reduce print rule to print (expression), by creating another rule
// todo: test for errors (3x string rule)
operacao: '!' | '-' | '&&' | '||' | '+' | '-'     | '+' | '*' | '/' | '=='
        | '!=' | '>=' | '<=' | '>' | '<' | '='
        | '+=' | '*='
        ;
// todo: describe operator with precedence, and specify them with rules

ID: [a-zA-Z]+[a-zA-Z0-9]*;
NUM: [0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
COMMENT:
    '//' .*? '\n' -> skip
    ;