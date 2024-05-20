# Sobre o Desafio

Este desafio visa coletar dados de um site específico
e integrá-los com Google BigQuery e Google Sheets

## 📦 Status do Desafio

- Em Resolução


## 🚀 Clonando Projeto

Nesta seção, explicaremos como você pode realizar o download e
rodar o projeto em sua máquina.

### 📋 Pré-requisitos

Antes de iniciar, verifique se você atende aos seguintes pré-requisitos:

- Python 3.11.2 ou superior
- Poetry
- Git

### 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clonando o Repositório:

```bash
git clone https://github.com/lspraciano/desafioBeAnalytic.git
```

2. No diretório raiz do projeto, instale as dependências com o comando:

```bash
cd desafioBeAnalytic
poetry install --no-root
```



## 📚 Tarefas

### 🔖 Coleta dos Dados

Para realizar a rotina de coletar os dados, estamos usando o selenium,
os dados são capturados e armazenados em uma lista de dicionário. Para
executar esta rotina podemos usar o comando abaixo

```
poetry run python -m routines.steam.get_all_sales_steam_data_routine
```


### 🔖 Integração com Google BigQuery
### 🔖 Disponibilização com Google Sheets
