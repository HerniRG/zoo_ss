from enum import Enum, auto
from collections import namedtuple

Datos_Entrada = namedtuple("Datos_Entrada", ("precio", "edad"))

class TipoEntrada(Enum):
    """
    primer valor de la tupla es el precio y el segundo la edad
    """
    BEBE = Datos_Entrada(0, 3)
    NIÑO = Datos_Entrada(14, 13)
    ADULTO = Datos_Entrada(23, 65)
    JUBILADO = Datos_Entrada(18, 99)
    INMORTAL = Datos_Entrada(0, float('inf'))

class Entrada():
    def __init__(self, edad_str):
        try:
            edad = int(edad_str)  # Intenta convertir el string a entero
        except ValueError:
            raise ValueError("La edad debe ser un número entero.")
        
        if edad < 0:
            raise ValueError("Solo edades mayores o iguales a 0.")
       
        self.edad = edad
        
        for tipo in TipoEntrada:
            if edad < tipo.value.edad:  # Accediendo al segundo elemento de la tupla para la edad
                self.tipo = tipo
                self.precio = tipo.value.precio  # Accediendo al primer elemento de la tupla para el precio
                break

class Grupo_Entrada():
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        
        # Asignar valor inicial 0 a cada tipo de entrada completo
        self.tipos_entrada = {}
        for tipo in TipoEntrada:
            self.tipos_entrada[tipo] = 0

    def add_entrada(self, edad):
        entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += entrada.precio
        self.tipos_entrada[entrada.tipo] += 1
        
    
    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo]
    
    def subtotal_tipo(self, tipo: TipoEntrada) -> int:
        subtotal = self.cantidad_entradas_por_tipo(tipo) * tipo.value.precio
        return subtotal
    

# Ejemplo de uso:
entrada = Entrada(25)
grupo = Grupo_Entrada()
grupo.add_entrada(15)
