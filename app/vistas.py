"""
               1         2         3        
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09                          
10    EDAD: 
11    CONF
"""
from simple_screen import Screen_manager, locate, Input
from collections import namedtuple
from app.modelos import Grupo_Entrada, TipoEntrada


class VistaGrupo():
    
    def __init__(self, grupo: Grupo_Entrada, x=1, y=1):
        self.grupo = grupo
        self.x = x
        self.y = y

    def paint(self):
        linea_pintada = self.y

        # Encabezado
        locate(self.x, linea_pintada,  "TIPO             PU     Q       TOTAL")
        linea_pintada += 1
        locate(self.x, linea_pintada,  "=====================================")
        linea_pintada += 1

        # Cuerpo tabla
        for tipo in TipoEntrada:
            nombre_tipo = f"{tipo.name: <14}"  # el nombre del tipo tendrá 14 caracteres
            precio = f"{tipo.value.precio:5.2f}"  # Accede al primer elemento de la tupla para el precio
            cantidad = f"{self.grupo.cantidad_entradas_por_tipo(tipo):2}"
            subtotal = f"{self.grupo.subtotal_tipo(tipo):7.2f}"
            locate(self.x, linea_pintada, f"{nombre_tipo}{precio}    {cantidad}     {subtotal}")
            linea_pintada += 1
        locate(self.x, linea_pintada, "-------------------------------------")
        linea_pintada += 1

        # Total de entradas y total de precio
        total_entradas = f"{self.grupo.num_entradas:3d}"
        total_precio = f"{self.grupo.total:8.2f}"
        locate(self.x, linea_pintada, f"                      {total_entradas}    {total_precio}")
        

class VistaInput():
    def __init__(self, etiqueta: str, x: int, y: int) -> None:
        self.etiqueta = etiqueta
        self.x = x
        self.y = y
        self.value = ""

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        self.value = Input()


