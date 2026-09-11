# ETA Unit Tests Challenge 1

Projeto de estudo de testes unitários com **pytest** para a validação de documentos brasileiros: **CEP**, **CPF** e **CNPJ**.
A validação de CEP combina a checagem de formato com a consulta a um serviço externo (ViaCEP) — simulada nos testes via `pytest-mock`.

## Estrutura do projeto

```
.
├── validador.py            # Implementação da classe Validador (CEP, CPF, CNPJ)
├── servico_correios.py     # Cliente para a API externa de consulta de CEP (ViaCEP)
├── test_validador.py       # Testes unitários do Validador (pytest)
├── test_servico_correios.py# Testes unitários do ServicoCorreios (pytest + mocks)
├── requirements.txt        # Dependências do projeto
├── assets/                 # Arquivos de estilo para o report
├── report.html             # Relatório de execução dos testes
├── .github/workflows/ci.yml# CI com GitHub Actions (testes + cobertura)
└── README.md
```

## Como executar os testes

### Pré-requisitos

- Python 3.x
- pytest instalado

Instale as dependências a partir do `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Rodando os testes

A partir da raiz do projeto, execute:

```bash
pytest -v
```

Com cobertura de linha:

```bash
pytest -v --cov=validador --cov=servico_correios --cov-report=term-missing
```

É possível gerar um relatório em HTML se o `pytest-html` estiver instalado:

```bash
pytest --html=report.html
```


## CI (GitHub Actions)

O workflow `.github/workflows/ci.yml` roda os testes com cobertura a cada push para `main` e em pull requests:

- checkouts do código
- configura o Python 3.13 com cache de `pip`
- instala as dependências do `requirements.txt`
- executa `pytest` com `--cov=validador --cov=servico_correios`