import pytest
from atividade import classifica_idade

@pytest.mark.crianca
def test_crianca():
    assert classifica_idade(12) == 'criança'

@pytest.mark.adolescente
def test_adolescente():
    assert classifica_idade(17) == 'adolescente'

@pytest.mark.adulto
def test_adulto():
    assert classifica_idade(57) == 'adulto'

@pytest.mark.idoso
def test_idoso():
    assert classifica_idade(80) == 'idoso'
