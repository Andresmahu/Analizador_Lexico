class Identifier:
    def __init__(self, nombre, fila, columna):
        self.tipo='id'
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return f"<{self.tipo},{self.nombre}, {self.fila}, {self.columna}>"

# Creating an object of the Identifier class
