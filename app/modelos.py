from enum import Enum, auto

class TipoEntrada(Enum):
    # BEBE = auto()
    # NIÑO = auto()
    # ADULTO = auto()
    # JUBILADO = auto()

    BEBE = {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0}
    NIÑO = {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0}
    ADULTO = {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0}
    JUBILADO = {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}

class Entrada():
    def __init__(self, edad: int) -> None:
        self.edad = edad
        if edad <= 2:
            self.tipo = TipoEntrada.BEBE
            self.precio = TipoEntrada.BEBE.value["PRECIO"]
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = 14
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = 23
        else: 
            self.tipo = TipoEntrada.JUBILADO
            self.precio = 18