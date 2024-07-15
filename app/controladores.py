from app.modelos import Grupo_Entrada
from app.vistas import VistaInput, VistaGrupo
from simple_screen import DIMENSIONS, cls, locate, Input

class Zoo():
    def __init__(self) -> None:
        self.grupo_entradas = Grupo_Entrada()
        self.x = (DIMENSIONS.w - 37) // 2
        self.vista_grupo = VistaGrupo(self.grupo_entradas, self.x, 1)
        self.entrada_edad = VistaInput("Edad: ", self.x, 12)
        self.entrada_seguir = VistaInput("Otra vez (S/N): ", self.x, 14)
    
    def run(self):
        while True:
            cls()
            self.vista_grupo.paint()
            self.entrada_edad.paint()
            edad = self.entrada_edad.value
            if edad == "":
                self.entrada_seguir.paint()
                respuesta = self.entrada_seguir.value
                if respuesta.lower() == "s":
                    grupo_entradas = Grupo_Entrada() # asigna por referencia
                    self.vista_grupo.grupo = grupo_entradas
                    continue
                else:
                    break
            try:
                self.vista_grupo.grupo.add_entrada(edad) # asigna por referencia  
            except ValueError as e:
                locate(self.x, 16, f"Error: {e}")
                locate(self.x, 18)
                Input("Pulse enter para continuar")
                
                     

        locate(self.x, 18)
        Input("Pulse enter para salir")
