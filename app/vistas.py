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
from modelos import Grupo_Entrada, TipoEntrada
from simple_screen import locate, Print, cls, Screen_manager, Input


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
            nombre_tipo = f"{tipo.name: <14}"  # Asegura que el nombre del tipo tenga 14 caracteres
            precio = f"{tipo.value['Precio']:5.2f}"
            cantidad = f"{self.grupo.cantidad_entradas_por_tipo(tipo):2}"
            subtotal = f"{self.grupo.subtotal_tipo(tipo):7.2f}"
            locate(self.x, (linea_pintada), f"{nombre_tipo}{precio}    {cantidad}     {subtotal}")
            linea_pintada += 1
        locate(self.x, linea_pintada, "-------------------------------------")
        linea_pintada += 1

        # Total de entradas y total de precio
        total_entradas = f"{self.grupo.num_entradas:3d}"
        total_precio = f"{self.grupo.total:8.2f}"
        locate(self.x, linea_pintada, f"                      {total_entradas}    {total_precio}")
        
        
if __name__ == "__main__":
    with Screen_manager:
        
        grupo = Grupo_Entrada()
        grupo.add_entrada(2)
        grupo.add_entrada(25)
        vg = VistaGrupo(grupo)
        vg.paint()
        
        grupo2 = Grupo_Entrada()
        grupo2.add_entrada(66)
        grupo2.add_entrada(98)
        grupo2.add_entrada(7)
        grupo2.add_entrada(190)
        vg2 = VistaGrupo(grupo2, 42)
        vg2.paint()

        Input()

