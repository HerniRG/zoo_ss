from app.modelos import Grupo_Entrada
from app.vistas import VistaEntrada, VistaGrupo
from simple_screen import DIMENSIONS, Screen_manager, cls, locate, Input



with Screen_manager:
    # Instanciamos lo necesario
    grupo_entradas = Grupo_Entrada()
    x = (DIMENSIONS.w - 37) // 2

    vista_grupo = VistaGrupo(grupo_entradas, x, 1)
    entrada_edad = VistaEntrada("Edad: ", x, 12)
    entrada_seguir = VistaEntrada("Otra vez (S/N): ", x, 14)



    # bucle de pantalla
    while True:
        cls()
        vista_grupo.paint()
        entrada_edad.paint()
        edad = entrada_edad.value
        if edad == "":
            entrada_seguir.paint()
            respuesta = entrada_seguir.value
            if respuesta == "S":
                grupo_entradas = Grupo_Entrada() # asigna por referencia
                vista_grupo.grupo = grupo_entradas
                continue
            else:
                break
        edad = int(edad)
        vista_grupo.grupo.add_entrada(edad) # asigna por referencia

    


    locate(1, DIMENSIONS.h - 2)
    #Input("Pulse enter para salir")


"""
from app.controladores import Zoo

zoo = Zoo()
zoo.run()
"""