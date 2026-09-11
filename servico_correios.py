import requests


class ServicoCorreios:
    """Cliente para o serviço externo de consulta de CEP dos Correios."""

    BASE_URL = "https://viacep.com.br/ws/{cep}/json/"

    def valida_cep_api(self, cep: str) -> bool:
        """Valida um CEP consultando um serviço externo fictício."""
        url = self.BASE_URL.format(cep=cep.strip())
        resposta = requests.get(url, timeout=5)

        if resposta.status_code != 200:
            return False

        dados = resposta.json()
        return "erro" not in dados