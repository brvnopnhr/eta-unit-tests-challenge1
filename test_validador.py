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
        "",              # vazio
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

# ----------------------------------------------------------------------
# CPF - casos válidos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cpf_valido",
    [
        "529.982.247-25",  # com máscara
        "52998224725",     # sem máscara
        "111.444.777-35",  # com máscara
        "11144477735",     # sem máscara
    ],
)
def test_validar_cpf_retorna_true_para_cpf_valido(validador, cpf_valido):
    assert validador.validar_cpf(cpf_valido) is True


# ----------------------------------------------------------------------
# CPF - casos inválidos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cpf_invalido",
    [
        "111.111.111-11",  # dígitos todos repetidos
        "123.456.789-00",  # dígitos verificadores incorretos
        "529.982.247-26",  # último dígito verificador alterado
        "5299822472",      # tamanho incorreto (faltando um dígito)
        "529982247255",    # tamanho incorreto (dígito a mais)
        "ABC.DEF.GHI-JK",  # não numérico
        "",                # vazio
    ],
)
def test_validar_cpf_retorna_false_para_cpf_invalido(validador, cpf_invalido):
    assert validador.validar_cpf(cpf_invalido) is False


# ----------------------------------------------------------------------
# CPF - exceção ValueError
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "valor_nao_texto",
    [
        52998224725,
        52998224725.0,
        None,
        ["529.982.247-25"],
        {"cpf": "529.982.247-25"},
    ],
)
def test_validar_cpf_levanta_value_error_para_valor_nao_texto(validador, valor_nao_texto):
    with pytest.raises(ValueError):
        validador.validar_cpf(valor_nao_texto)
# ----------------------------------------------------------------------
# CNPJ - casos válidos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cnpj_valido",
    [
        "11.222.333/0001-81",   # com máscara
        "11222333000181",       # sem máscara
        "04.252.011/0001-10",   # com máscara
        "04252011000110",       # sem máscara
    ],
)
def test_validar_cnpj_retorna_true_para_cnpj_valido(validador, cnpj_valido):
    assert validador.validar_cnpj(cnpj_valido) is True


# ----------------------------------------------------------------------
# CNPJ - casos inválidos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cnpj_invalido",
    [
        "11.111.111/1111-11",  # dígitos todos repetidos
        "11.222.333/0001-00",  # dígitos verificadores incorretos
        "11.222.333/0001-82",  # último dígito verificador alterado
        "1122233300018",       # tamanho incorreto (faltando um dígito)
        "112223330001811",     # tamanho incorreto (dígito a mais)
        "AB.CDE.FGH/IJKL-MN",  # não numérico
        "",                    # vazio
    ],
)
def test_validar_cnpj_retorna_false_para_cnpj_invalido(validador, cnpj_invalido):
    assert validador.validar_cnpj(cnpj_invalido) is False


# ----------------------------------------------------------------------
# CNPJ - exceção ValueError
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "valor_nao_texto",
    [
        11222333000181,
        11222333000181.0,
        None,
        ["11.222.333/0001-81"],
        {"cnpj": "11.222.333/0001-81"},
    ],
)
def test_validar_cnpj_levanta_value_error_para_valor_nao_texto(validador, valor_nao_texto):
    with pytest.raises(ValueError):
        validador.validar_cnpj(valor_nao_texto)
