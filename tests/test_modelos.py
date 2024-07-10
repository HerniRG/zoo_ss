import pytest
from app.modelos import Entrada, TipoEntrada, Grupo_Entrada  

def test_crear_entrada():
    entrada = Entrada(2)
    assert entrada.tipo == TipoEntrada.BEBE
    assert entrada.precio == 0

    entrada = Entrada(12)
    assert entrada.tipo == TipoEntrada.NIÑO
    assert entrada.precio == 14

    entrada = Entrada(35)
    assert entrada.tipo == TipoEntrada.ADULTO
    assert entrada.precio == 23

    entrada = Entrada(70)
    assert entrada.tipo == TipoEntrada.JUBILADO
    assert entrada.precio == 18

def test_crear_grupo_entradas():
    grupo = Grupo_Entrada()
    assert grupo.total == 0
    assert grupo.num_entradas == 0

def test_anadir_entradas_a_grupo():
    grupo = Grupo_Entrada()
    grupo.add_entrada(23)
    assert grupo.num_entradas == 1
    assert grupo.total == 23 

    grupo.add_entrada(12)
    assert grupo.num_entradas == 2
    assert grupo.total == 37

    grupo.add_entrada(70)
    assert grupo.num_entradas == 3
    assert grupo.total == 55

    grupo.add_entrada(2)
    assert grupo.num_entradas == 4
    assert grupo.total == 55

def test_provocar_errores():
    grupo = Grupo_Entrada()

    with pytest.raises(ValueError):
        grupo.add_entrada(-9)

    with pytest.raises(TypeError) as excinfo:
        grupo.add_entrada("hola")
    assert str(excinfo.value) == "La edad debe ser un número entero."

    
    with pytest.raises(ValueError) as excinfo:
        Entrada(-2)
    assert str(excinfo.value) == "Solo edades mayores o iguales a 0."

    with pytest.raises(TypeError):
        Entrada("hola")

def test_cantidad_entradas_por_tipo():
    grupo = Grupo_Entrada()
    
    grupo.add_entrada(10)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.NIÑO) == 1

    grupo.add_entrada(36)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.ADULTO) == 1

    grupo.add_entrada(9)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.NIÑO) == 2

    grupo.add_entrada(99)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.JUBILADO) == 1

    grupo.add_entrada(1)
    assert grupo.cantidad_entradas_por_tipo(TipoEntrada.BEBE) == 1

def test_subtotal_por_tipo():
    grupo = Grupo_Entrada()

    grupo.add_entrada(10)
    assert grupo.subtotal_tipo(TipoEntrada.NIÑO) == 14

    grupo.add_entrada(11)
    assert grupo.subtotal_tipo(TipoEntrada.NIÑO) == 28