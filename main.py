from scanner.scanner import read_file, scannerFunction, generadorTokensSinProcesar, clasificadorDeTokens
from Parser.Parser import *
path = "ejemplo_prueba_4.txt"
def run(path):
    texto=read_file(path)
    tokens = generadorTokensSinProcesar(texto)
    salida = clasificadorDeTokens(tokens)
    #for i in salida:
        #print(i)
    lines=LineSeparatorName(salida)
    linesObject=LineSeparatorObject(salida)
    ParserExecute(lines,linesObject)
if __name__ == '__main__':
    run(path)

