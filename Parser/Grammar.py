PythonGrammar= {
'STMNT':[['SIMPLESTMNT'],['COMPOUNDSTMNT'],['']],
'SIMPLESTMNT':[['ASSIGNMENT','NEWLINE']],
'COMPOUNDSTMNT':[['FOR','WHILE','IF','DEFFUNC','NEWLINE']],
'FOR': [['for', 'id', 'in','FOR-']],
'FOR-':[['id', 'tk_dos_puntos'],['range', 'tk_par_izq', 'RANGESTMT', ]],
'WHILE':[['while','IFSTMT','tk_dos_puntos','STMNT']],
'DEFFUNC':[['def','id','tk_par_izq','PARAMS','tk_dos_puntos','STMNT','RETURNSTMNT']],
'RETURNSTMNT':[['return','FUNC'],['return','id'],['return','ARITMETHIC'],['return','VALUES']],
'RANGESTMT':[['id','tk_par_der', 'tk_dos_puntos'],['len','tk_par_izq','id','tk_par_der','tk_par_der', 'tk_dos_puntos'],['tk_entero']],
'IF':[['if','IFSTMT']],
'IF-':[['else','tk_dos_puntos','STMNT'],['elif','IFSTMT','tk_dos_puntos','STMNT','IF-']],
'IFSTMT':[['id','IFSTMT-'],
          ['ARITMETHIC','IFSTMT-'], ['FUNC','tk_dos_puntos']],
'IFSTMT-':[['COMPARISON','IFSTMT--']],
'IFSTMT--':[['id','tk_dos_puntos'],['VALUES'],['NUMBER']],
'DATATYPE':[['int'],['float'],['complex'],['str'],['bool'],['list'],['tuple'],['set']],
'NUMBER':[['tk_entero'],['tk_float'],['tk_complejo']],
'COMPARISON':[['tk_equal'],['tk_no_equal'],['tk_less_equal'],['tk_greater_equal'],
              ['tk_less'],['tk_greater']],
'ARITMETHIC':[['id','NOP','NUMBER'],['id','NOP','id'],['NUMBER','NOP','NUMBER'],
              ['NUMBER','NOP','id']],
'NOP': [['tk_plus'],['tk_minus'],['tk_star'],['tk_slash'],['tk_double_star'],['tk_percent']],
'ASSIGNMENT': [['id','ASSIGNOP','VALUES'],['id','ASSIGNOP','FUNC']],
'ASSIGNOP':[['tk_minus_equal'],['tk_plus_equal'],['tk_slash_equal'],['tk_star_equal'],['tk_percent_equal'],['tk_asing']],
'FUNC': [['id','tk_par_izq','PARAMS','tk_par_der']],
'PARAMS':[['FPARAMS'],['FPARAMS','tk_comma','PARAMS']],
'FPARAMS': [['id'],['VALUES'],['FUNC']],
'DPARAMS': [['id'],['id','tk_dos_puntos','DATATYPE']],
'VALUES': [['tk_entero'],['tk_float'],['tk_complejo'],['tk_cadena']]
    }


