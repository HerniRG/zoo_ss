from enum import Enum, auto

"""De esta manera se pueden cambiar tipos de entrada, las edades y los precios 
de las entradas en el comienzo del código sin cambiar nada por medio"""

class TipoEntrada(Enum):
    """
    Enum TipoEntrada. En este caso los values son los precios de entrada y limite de edad de cada tipo.
    """
    BEBE = {"Precio": 0, "Edad": 3}
    NIÑO = {"Precio": 14, "Edad": 13}
    ADULTO = {"Precio": 23, "Edad": 65}
    JUBILADO = {"Precio": 18, "Edad": 99}
    INMORTAL = {"Precio": 0, "Edad": float('inf')}

class Entrada():
    def __init__(self, edad):
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        elif edad < 0:
            raise ValueError("Solo edades mayores o iguales a 0.")
       
        self.edad = edad
        
        for tipo in TipoEntrada:
            if edad < tipo.value["Edad"]:
                self.tipo = tipo
                self.precio = tipo.value["Precio"] # no hace falta pero lo dejo para simplicidad posterior en Grupo_Entrada
                break          

class Grupo_Entrada():
    def __init__(self):
        self.total = 0
        self.num_entradas = 0
        self.tipos_entrada = {tipo: 0 for tipo in TipoEntrada} # Asignar valor inicial 0 a cada tipo de entrada completo (<TipoEntrada.BEBE: {'Precio': 0, 'Edad': 3}>: 0)
        
        # self.tipos_entrada = {}          dictionary comprehension: es lo mismo que la linea de arriba :)
        # for tipo in TipoEntrada:
        #     self.tipos_entrada[tipo] = 0  

    def add_entrada(self, edad):
        entrada = Entrada(edad)
        self.num_entradas += 1
        self.total += entrada.precio
        self.tipos_entrada[entrada.tipo] += 1
        
    
    def cantidad_entradas_por_tipo(self, tipo: TipoEntrada) -> int:
        return self.tipos_entrada[tipo] # devuelve los valores del diccionario con la clave tipo que le pasamos de argumento
    
    def subtotal_tipo(self, tipo: TipoEntrada) -> int:
        subtotal = self.cantidad_entradas_por_tipo(tipo) * tipo.value["Precio"]
        return subtotal
    

entrada = Entrada(25)
grupo = Grupo_Entrada()
grupo.add_entrada(15)