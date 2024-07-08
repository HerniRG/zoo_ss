from app.modelos import Entrada, TipoEntrada  

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

def test_crear_entradas_negativas():
    entrada = Entrada(-2)
    