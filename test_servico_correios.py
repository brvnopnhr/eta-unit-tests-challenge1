import pytest
import requests

from servico_correios import ServicoCorreios


@pytest.fixture
def servico_correios() -> ServicoCorreios:
    """Fornece uma instância da classe ServicoCorreios para os testes."""
    return ServicoCorreios()


# ----------------------------------------------------------------------
# ServicoCorreios.valida_cep_api - caso positivo
# ----------------------------------------------------------------------

def test_valida_cep_api_retorna_true_quando_cep_e_encontrado(mocker):
    """Simula a chamada à API retornando sucesso (CEP válido)."""
    mock_servico = mocker.patch("servico_correios.ServicoCorreios")
    mock_servico.return_value.valida_cep_api.return_value = True

    resultado = mock_servico.return_value.valida_cep_api("69000-000")

    assert resultado is True
    mock_servico.return_value.valida_cep_api.assert_called_once_with("69000-000")


# ----------------------------------------------------------------------
# ServicoCorreios.valida_cep_api - casos negativos
# ----------------------------------------------------------------------

@pytest.mark.parametrize(
    "cep_invalido",
    [
        "99999-999",  # CEP inexistente no serviço
        "ABCDE-FGH",  # CEP não numérico
        "",           # CEP vazio
    ],
)
def test_valida_cep_api_retorna_false_quando_cep_nao_e_encontrado(
    mocker, cep_invalido
):
    """Simula a chamada à API retornando falha na validação."""
    mock_servico = mocker.patch("servico_correios.ServicoCorreios")
    mock_servico.return_value.valida_cep_api.return_value = False

    resultado = mock_servico.return_value.valida_cep_api(cep_invalido)

    assert resultado is False
    mock_servico.return_value.valida_cep_api.assert_called_once_with(cep_invalido)


# ----------------------------------------------------------------------
# ServicoCorreios.valida_cep_api - caso de exceção
# ----------------------------------------------------------------------

def test_valida_cep_api_lanca_http_error_quando_servico_externo_falha(
    servico_correios, mocker
):
    """Simula erro de conexão com o serviço externo ao validar o CEP."""
    mocker.patch(
        "servico_correios.requests.get",
        side_effect=requests.exceptions.HTTPError("Erro de conexão com o serviço"),
    )

    with pytest.raises(requests.exceptions.HTTPError):
        servico_correios.valida_cep_api("69000-000")