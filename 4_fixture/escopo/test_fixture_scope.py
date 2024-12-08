import pytest

# Neste tipo de escopo, cada função que usar esta fixture irá criar e destruir os dados.
@pytest.fixture(scope="function")
def fixture_function():
    return 10

# Neste tipo de escopo, a fixture será criada uma vez para cada módulo e estará disponível para todas as 
# funções de testes dentro deste módulo e só depois fará o teardown.
@pytest.fixture(scope="module")
def fixture_module():
    return 20

# Neste tipo de escopo, a fixture ficará dispinível para uma sessão. Todas as funções de testes que que a chamarem 
# terão a mesma instância da fixture e só no fim o teardown será feito.
@pytest.fixture(scope="session")
def fixture_session():
    return 30

def test_1(fixture_function):
    assert fixture_function == 10

def test_2(fixture_function, fixture_module):
    assert fixture_function == 10
    assert fixture_module == 20

def test_3(fixture_module, fixture_session):
    assert fixture_module == 20
    assert fixture_session == 30


