import re


class Validador:
    """Classe utilitária para validação de CEP, CPF e CNPJ."""

    @staticmethod
    def _garantir_texto(valor) -> None:
        """Levanta ValueError se `valor` não for uma string."""
        if not isinstance(valor, str):
            raise ValueError("O valor informado deve ser um texto (str).")

    @staticmethod
    def _apenas_digitos(texto: str) -> str:
        """Remove qualquer caractere que não seja dígito."""
        return re.sub(r"\D", "", texto)

    @staticmethod
    def _calcular_digito_cpf(digitos: str, peso_inicial: int) -> int:
        """Calcula um dígito verificador do CPF."""
        soma = sum(
            int(digito) * peso
            for digito, peso in zip(digitos, range(peso_inicial, 1, -1))
        )
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    @staticmethod
    def _calcular_digito_cnpj(digitos: str, pesos: list) -> int:
        """Calcula um dígito verificador do CNPJ a partir de uma lista de pesos."""
        soma = sum(int(digito) * peso for digito, peso in zip(digitos, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # ------------------------------------------------------------------
    # CEP
    # ------------------------------------------------------------------

    def validar_cep(self, cep) -> bool:
        self._garantir_texto(cep)

        # Verifica se, exceto pelos dígitos, só há hífen na formatação
        texto_limpo = cep.strip()
        if not re.fullmatch(r"\d{5}-?\d{3}", texto_limpo):
            return False

        digitos = self._apenas_digitos(texto_limpo)
        return len(digitos) == 8

    # ------------------------------------------------------------------
    # CPF
    # ------------------------------------------------------------------

    def validar_cpf(self, cpf) -> bool:
        self._garantir_texto(cpf)

        texto_limpo = cpf.strip()
        if not re.fullmatch(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", texto_limpo):
            return False

        digitos = self._apenas_digitos(texto_limpo)

        if len(digitos) != 11:
            return False

        # CPFs com todos os dígitos iguais são inválidos (ex: 00000000000)
        if digitos == digitos[0] * 11:
            return False

        primeiro_digito = self._calcular_digito_cpf(digitos[:9], 10)
        segundo_digito = self._calcular_digito_cpf(digitos[:10], 11)

        return digitos[-2:] == f"{primeiro_digito}{segundo_digito}"

    # ------------------------------------------------------------------
    # CNPJ
    # ------------------------------------------------------------------

    def validar_cnpj(self, cnpj) -> bool:

        self._garantir_texto(cnpj)

        texto_limpo = cnpj.strip()
        if not re.fullmatch(
            r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}", texto_limpo
        ):
            return False

        digitos = self._apenas_digitos(texto_limpo)

        if len(digitos) != 14:
            return False

        if digitos == digitos[0] * 14:
            return False

        pesos_primeiro_digito = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos_segundo_digito = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        primeiro_digito = self._calcular_digito_cnpj(
            digitos[:12], pesos_primeiro_digito
        )
        segundo_digito = self._calcular_digito_cnpj(
            digitos[:13], pesos_segundo_digito
        )

        return digitos[-2:] == f"{primeiro_digito}{segundo_digito}"


# ----------------------------------------------------------------------
# Exemplo de uso
# ----------------------------------------------------------------------
if __name__ == "__main__":
    validador = Validador()

    # CEP
    print(validador.validar_cep("69000-000"))   # True
    print(validador.validar_cep("6900-000"))    # False (tamanho incorreto)

    # CPF
    print(validador.validar_cpf("52998224725"))      # True
    print(validador.validar_cpf("111.111.111-11"))   # False (dígitos repetidos)

    # CNPJ
    print(validador.validar_cnpj("11222333000181"))       # True
    print(validador.validar_cnpj("11.111.111/1111-11"))   # False (dígitos repetidos)

    # ValueError
    try:
        validador.validar_cpf(12345678900)
    except ValueError as erro:
        print(f"Erro esperado: {erro}")