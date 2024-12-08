def is_positive(numero):
    return numero > 0


def test_eh_positivo():
    # Este teste irá falhar se o segundo assert for descomentado, pois dentro de um teste, para que o teste seja aprovado, é necessário que todos os asserts serjam verdadeiros
    # Por este motivo o segundo assert está comentado, apenas para servir de referência de estudo.
    assert is_positive(5) is True
    # assert is_positive(5) is False

