from Parser.Grammar import PythonGrammar
from tokens.identifier_class import Identifier


def LineSeparatorName(TokenList):
    FilaActual=TokenList[0].fila
    Filas=[]
    Fila=[]
    for token in TokenList:
        if FilaActual==token.fila:
            if isinstance(token,Identifier):
                Fila.append(token.tipo)
            else:
                Fila.append(token.nombre)
        else:
            Filas.append(Fila)
            Fila=[]
            if isinstance(token, Identifier):
                Fila.append(token.tipo)
            else:
                Fila.append(token.nombre)
            FilaActual=token.fila
    Filas.append(Fila)
    return Filas
def LineSeparatorObject(TokenList):
    FilaActual=TokenList[0].fila
    Filas=[]
    Fila=[]
    for token in TokenList:
        if FilaActual==token.fila:
            Fila.append(token)
        else:
            Filas.append(Fila)
            Fila=[]
            Fila.append(token)
            FilaActual=token.fila
    Filas.append(Fila)
    return Filas
def Parser(Rule,Line,LineObject):
    comprobacion=False
    for lista in PythonGrammar[Rule]:
        for i in range(len(lista)):
            print(Rule,'Regla')
            print(lista[i],'gramtica')
            print(Line[i], 'entrada')
            print(i)
            if lista[i].isupper():
                if not(Parser(lista[i], Line[i:], LineObject[i:])):
                    return False
            else:
                if lista[i]==Line[i]:
                    comprobacion=True
                    continue
                else:
                    if comprobacion:
                        print(
                            f'<{LineObject[i].fila},{LineObject[i].columna}> Error sintactico: se encontro "{Line[i]}" se esperaba "{lista[i]}"')
                        return False
                    if PythonGrammar[Rule].index(lista)==len(PythonGrammar[Rule])-1:
                        print(
                            f'<{LineObject[i].fila},{LineObject[i].columna}> Error sintactico: se encontro "{Line[i]}" se esperaba "{lista[i]}"')
                        return False
                    elif len(PythonGrammar[Rule])>1:
                        break
                    else:
                        print(
                            f'<{LineObject[i].fila},{LineObject[i].columna}> Error sintactico: se encontro "{Line[i]}" se esperaba "{lista[i]}"')
                        return False
        if comprobacion:
            break
    return True
def ParserExecute(Line,LineObject):
    for i in range(len(LineObject)):
        match Line[i][0]:
            case 'for':
                if not(Parser("FOR",Line[i],LineObject[i])):
                    return
            case 'if':
                if not (Parser("IF", Line[i], LineObject[i])):
                    return
            case 'def':
                if not (Parser("DEFFUNC", Line[i], LineObject[i])):
                    return
        if isinstance(LineObject[i][0],Identifier):
            if LineObject[i][1].nombre=='tk_par_izq':
                if not (Parser("FUNC", Line[i], LineObject[i])):
                    return
            else:
                if not (Parser("ASSIGNMENT", Line[i], LineObject[i])):
                    return
        if i>=1:
            if LineObject[i-1][-1].nombre == 'tk_dos_puntos':
                if LineObject[i][0].columna <= LineObject[i-1][0].columna:
                    print(f'<{LineObject[i][0].fila},{LineObject[i][0].columna}>Error sintactico: falla de identacion')
                    return
    print("El analisis sintactico ha finalizado exitosamente.")




