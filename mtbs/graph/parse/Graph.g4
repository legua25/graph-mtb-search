grammar Graph;

// -- PARSER ----------------------------------------------------------------
graph: 
    graph_meta_properties
    graph_nodes?
;

graph_meta_properties: name = identifier props = meta_properties?;
meta_properties: 
    '{'
        (props += meta_property (',' props += meta_property)*)?
    '}'
;
meta_property: key = identifier ':' value = meta_value;
meta_value:
    string = String | 
    number = Number | 
    meta = meta_properties
;

graph_nodes: nodes += graph_node+;
graph_node: name = identifier props = meta_properties? (':' neighbors += identifier (',' neighbors += identifier)*)? ';';
identifier: name = ID;

// -- LEXER -----------------------------------------------------------------
Number: 
    '0' | 
    [-]? [1-9] [0-9]* | 
    [-]? [0-9]* '.' [0-9]+
;
String: ['] (Escape | ~[\\'])* ['];
fragment Escape: '\\' ([\\'nrt] | [u] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9] [a-fA-F0-9]);

Comment: '#' ~[\n\r]* -> skip;
Whitespace: [ \t\u000C] -> skip;
Newline: ('\n' | '\r' '\n'?) -> skip;
ID: [a-zA-Z_] [a-zA-Z_\-0-9]*;
