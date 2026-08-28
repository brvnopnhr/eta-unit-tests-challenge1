import pytest

from validador import Validador

@pytest.fixture
def validador() -> Validador:
    """Fornece uma instância da classe Validador para os testes."""
    return Validador()


# ----------------------------------------------------------------------
# CEP - casos válidos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cep_valido",
    [
        "69000-000",   # com máscara (hífen)
        "69000000",    # sem máscara
        "01310-100",   # com máscara
        "01310100",    # sem máscara
    ],
)
def test_validar_cep_retorna_true_para_cep_valido(validador, cep_valido):
    assert validador.validar_cep(cep_valido) is True


# ----------------------------------------------------------------------
# CEP - casos inválidos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cep_invalido",
    [
        "6900-000",      # tamanho incorreto (faltando um dígito)
        "690000000",     # tamanho incorreto (dígito a mais)
        "69000-0000",    # tamanho incorreto (dígito a mais após o hífen)
        "ABCDE-FGH",     # não numérico
        "69000_000",     # separador incorreto
        "",               # vazio
    ],
)
def test_validar_cep_retorna_false_para_cep_invalido(validador, cep_invalido):
    assert validador.validar_cep(cep_invalido) is False


# ----------------------------------------------------------------------
# CEP - exceção ValueError
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "valor_nao_texto",
    [
        69000000,
        69000000.0,
        None,
        ["69000-000"],
        {"cep": "69000-000"},
    ],
)
def test_validar_cep_levanta_value_error_para_valor_nao_texto(validador, valor_nao_texto):
    with pytest.raises(ValueError):
        validador.validar_cep(valor_nao_texto)
