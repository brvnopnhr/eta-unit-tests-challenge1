# ETA Unit Tests Challenge 1

Projeto de estudo de testes unitários com **pytest** para a validação de documentos brasileiros: **CEP**, **CPF** e **CNPJ**.


## Estrutura do projeto

```
.
├── validador.py        # Implementação da classe Validador
├── test_validador.py   # Testes unitários (pytest)
├── assets/             # Arquivos de estilo para o report
├── report.html         # Relatório de execução dos testes
└── README.md
```

## Como executar os testes

### Pré-requisitos

- Python 3.x
- pytest instalado

Instale o pytest e opcionalmente pytest-html:

```bash
pip install pytest
pip install pytest-html
```

### Rodando os testes

A partir da raiz do projeto, execute:

```bash
pytest -v
```

É possível gerar um relatório em HTMLse o `pytest-html` estiver instalado:

```bash
pytest --html=report.html
```
