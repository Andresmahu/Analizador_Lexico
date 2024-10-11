#special character tokens
character_special = {
    ')': 'tk_par_der',
    '(': 'tk_par_izq',
    ']': 'tk_sqb_der',
    '[': 'tk_sqb_izq',
    ':': 'tk_dos_puntos',
    ',': 'tk_comma',
    ';': 'tk_punto_comma',
    '+': 'tk_plus',
    '-': 'tk_minus',
    '*': 'tk_star',
    '/': 'tk_slash',
    '|': 'tk_vbar',
    '&': 'tk_amper',
    '<': 'tk_less',
    '>': 'tk_greater',
    '=': 'tk_asing',
    '.': 'tk_punto',
    '%': 'tk_percent',
    '}': 'tk_brace_der',
    '{': 'tk_brace_izq',
    '==': 'tk_equal',
    '!=': 'tk_no_equal',
    '<=': 'tk_less_equal',
    '>=': 'tk_greate_equal',
    '^': 'tk_circumflex',
    '<<': 'tk_shift_izq',
    '>>': 'tk_shift_der',
    '**': 'tk_double_star',
    '+=': 'tk_plus_equal',
    '-=': 'tk_mine_equal',
    '*=': 'tk_star_equal',
    '/=': 'tk_slash_equal',
    '%=': 'tk_percent_equal',
    '&=': 'tk_amper_equal',
    '|=': 'tk_vabar_equal',
    '^=': 'tk_circum_flex_equal',
    '<<=': 'tk_shift_equal_izq',
    '>>=': 'tk_shift_equal_der',
    '**=': 'tk_double_start_equal',
    '//': 'tk_double_slash',
    '//=': 'tk_double_slash_equal',
    '@': 'tk_at',
    '@=': 'tk_at_equal',
    '->': 'tk_ejecuta',
    '...': 'tk_ellipsis',
    ':=': 'tk_dos_puntos_equal'
}
#reserved words
word_reserved={
    'open':'open',
    'False': 'False',
    'None': 'None',
    'True': 'True',
    'and': 'and',
    'as': 'as',
    'assert': 'assert',
    'async': 'async',
    'await': 'await',
    'break': 'break',
    'class': 'class',
    'continue': 'continue',
    'def': 'def',
    'del': 'del',
    'elif': 'elif',
    'else': 'else',
    'except': 'except',
    'finally': 'finally',
    'for': 'for',
    'from': 'from',
    'global': 'global',
    'if': 'if',
    'import': 'import',
    'in': 'in',
    'is': 'is',
    'lambda': 'lambda',
    'nonlocal': 'nonlocal',
    'not': 'not',
    'or': 'or',
    'pass': 'pass',
    'raise': 'raise',
    'return': 'return',
    'try': 'try',
    'while': 'while',
    'with': 'with',
    'yield': 'yield',
    'object': 'object',
    'self':'self',
    'print': 'print',
    'input':'input',
    'len':'len'
}
#metodos
methods={
    'append': 'append',
    'extend': 'extend',
    'insert': 'insert',
    'reverse': 'reverse',
    'sort': 'sort',
    'fromkeys': 'fromkeys',
    'get': 'get',
    'items': 'items',
    'keys': 'keys',
    'popitem': 'popitem',
    'setdefault': 'setdefault',
    'values': 'values',
    'add': 'add',
    'clear': 'clear',
    'copy': 'copy',
    'difference': 'difference',
    'difference_update': 'difference_update',
    'discard': 'discard',
    'intersection': 'intersection',
    'intersection_update': 'intersection_update',
    'isdisjoint': 'isdisjoint',
    'issubset': 'issubset',
    'issuperset': 'issuperset',
    'pop': 'pop',
    'remove': 'remove',
    'symmetric_difference': 'symmetric_difference',
    'symmetric_difference_update': 'symmetric_difference_update',
    'union': 'union',
    'update': 'update',
    'capitalize': 'capitalize',
    'casefold': 'casefold',
    'center': 'center',
    'count': 'count',
    'encode': 'encode',
    'endswith': 'endswith',
    'expandtabs': 'expandtabs',
    'find': 'find',
    'format': 'format',
    'format_map': 'format_map',
    'index': 'index',
    'isalnum': 'isalnum',
    'isalpha': 'isalpha',
    'isascii': 'isascii',
    'isdecimal': 'isdecimal',
    'isdigit': 'isdigit',
    'isidentifier': 'isidentifier',
    'islower': 'islower',
    'isnumeric': 'isnumeric',
    'isprintable': 'isprintable',
    'isspace': 'isspace',
    'istitle': 'istitle',
    'isupper': 'isupper',
    'join': 'join',
    'ljust': 'ljust',
    'lower': 'lower',
    'lstrip': 'lstrip',
    'maketrans': 'maketrans',
    'partition': 'partition',
    'replace': 'replace',
    'rfind': 'rfind',
    'rindex': 'rindex',
    'rjust': 'rjust',
    'rpartition': 'rpartition',
    'rsplit': 'rsplit',
    'rstrip': 'rstrip',
    'split': 'split',
    'splitlines': 'splitlines',
    'startswith': 'startswith',
    'strip': 'strip',
    'swapcase': 'swapcase',
    'title': 'title',
    'translate': 'translate',
    'upper': 'upper',
    'zfill': 'zfill',
    'bit_length': 'bit_length',
    'to_bytes': 'to_bytes',
    'from_bytes': 'from_bytes',
    'is_integer': 'is_integer',
    'hex': 'hex',
    'conjugate': 'conjugate',
    'real': 'real',
    'imag': 'imag'
}
data_types = {
    "int": "int",
    "float": "float",
    "complex": "complex",
    "bool": "bool",
    "str": "str",
    "list": "list",
    "tuple": "tuple",
    "set": "set",
    "dict": "dict",
    "NoneT": "None",
    "bytes": "bytes",
    "bytearray": "bytearray",
    "range": "range",
    "frozenset": "frozenset",
}
