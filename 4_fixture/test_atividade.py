import pytest

def soma_dobro(numero):
    if numero is None:
        return 0
    if len(numero) > 0:
        soma = sum(x * 2 for x in numero)
        return soma
    else:
        return 0


@pytest.fixture
def data_fixture():
    return [10, 20]


def test_soma_numero(data_fixture):
    # O resultado da fixture é 60
    assert soma_dobro(data_fixture) == 60

def test_soma_numero_vazio(data_fixture):
    # A lista vazia deve retornar zero.
    assert soma_dobro(data_fixture.clear()) == 0