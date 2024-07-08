from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = auto()
    NIÑO = auto()
    ADULTO = auto()
    JUBILADO = auto()
    NO_VALIDO = auto()

    # BEBE = {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0}
    # NIÑO = {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0}
    # ADULTO = {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0}
    # JUBILADO = {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}



class Entrada():
    def __init__(self, edad: int):
        self.edad = edad
        if edad < 0:
            self.tipo = TipoEntrada.NO_VALIDO
            self.precio = 0
        elif edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = 0
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else: 
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18

class Grupo_Entrada():
    def __init__(self):
        self.total = 0
        self.num_entradas = 0

    def add_entrada(self, edad):
        """En la funcion de la edad, crear una entrada e incrementar 
        entradas con el precio de la entrada nueva incrementar el total"""

        entrada = Entrada(edad)
        
        if entrada.tipo != TipoEntrada.NO_VALIDO:
            self.num_entradas += 1
            self.total += entrada.precio