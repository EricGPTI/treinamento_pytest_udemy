def somar(a, b):
    return a + b


def comprimeiro(lista):
    return len(lista)


def test_somar_e_comprimento():
    assert somar(3, 2) == 5
    assert comprimeiro([1, 2, 3, 4, 5]) == 5