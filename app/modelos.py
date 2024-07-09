from enum import Enum, auto

class TipoEntrada(Enum):
    BEBE = 0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18

    # BEBE = {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0}
    # NIÑO = {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0}
    # ADULTO = {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0}
    # JUBILADO = {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}



class Entrada():
    def __init__(self, edad: int):

        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        elif edad < 0:
            raise ValueError("Solo edades mayores o iguales a 0.")
       
        self.edad = edad
        
        if edad < 3:
            self.tipo = TipoEntrada.BEBE
            self.precio = TipoEntrada.BEBE.value
        elif edad < 13:
            self.tipo = TipoEntrada.NIÑO
            self.precio = TipoEntrada.NIÑO.value
        elif edad < 65:
            self.tipo = TipoEntrada.ADULTO
            self.precio = TipoEntrada.ADULTO.value
        else: 
            self.tipo = TipoEntrada.JUBILADO
            self.precio = TipoEntrada.JUBILADO.value

class Grupo_Entrada():
    def __init__(self):
        self.total = 0
        self.num_entradas = 0

    def add_entrada(self, edad):
        entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += entrada.precio