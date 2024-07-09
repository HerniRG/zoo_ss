from enum import Enum, auto

"""De esta manera se pueden cambiar las edades, tipos de entrada y los precios 
de las entradas en el comienzo del código sin cambiar nada por medio"""

class TipoEntrada(Enum):
    """
    Enum TipoEntrada. En este caso los values son los precios de entrada de cada tipo.
    """
    BEBE = 0
    NIÑO = 14
    ADULTO = 23
    JUBILADO = 18

class Entrada():
    edades = [3, 13, 65, float('inf')] # Los limites de las edades en lista para iterar posteriormente

    def __init__(self, edad: int):
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        elif edad < 0:
            raise ValueError("Solo edades mayores o iguales a 0.")
       
        self.edad = edad
        tipos = list(TipoEntrada) # [<TipoEntrada.BEBE: 0>, <TipoEntrada.NIÑO: 14>, <TipoEntrada.ADULTO: 23>, <TipoEntrada.JUBILADO: 18>]
        for indice, limite_edad in enumerate(self.edades):
            if edad < limite_edad:
                self.tipo = tipos[indice] # TipoEntrada.BEBE, TipoEntrada.NIÑO, TipoEntrada.ADULTO, TipoEntrada.JUBILADO
                self.precio = tipos[indice].value # 0, 14, 23, 18
                break             

class Grupo_Entrada():
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {TipoEntrada.BEBE: 0, TipoEntrada.NIÑO: 0, TipoEntrada.ADULTO: 0, TipoEntrada.JUBILADO: 0}


    def add_entrada(self, edad):
        entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += entrada.precio
        self.tipos_entrada[entrada.tipo] += 1
        
    
    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada):
        return self.tipos_entrada[tipo]






    
