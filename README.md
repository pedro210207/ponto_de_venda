# Sistema de Ponto de Venda (PDV) - Python + MySQL

Sistema de Ponto de Venda desenvolvido em Python com integração ao MySQL para registro e análise de vendas.

Este projeto simula um pequeno sistema comercial com funcionalidades de cadastro, listagem, remoção, análise de vendas e processamento de dados com Pandas.

---

## Funcionalidades

- Cadastro de vendas
- Listagem de vendas
- Remoção de vendas
- Cálculo automático do valor total (quantidade × valor)
- Resumo analítico com:
  - Total geral vendido
  - Ticket médio
  - Produto mais vendido
  - Vendas agrupadas por data

---

## Tecnologias Utilizadas

- Python
- MySQL
- Pandas

---

## Estrutura do Projeto

- `database.py` → Conexão com o banco de dados
- `crud.py` → Operações de cadastro, listagem e exclusão
- `analytics.py` → Métricas e análises com Pandas
- `main.py` → Menu principal
- `database.sql` → Script de criação do banco

---

## Como rodar o projeto

### 1. Instalar dependências

```bash
pip install mysql-connector-python pandas
```

### 2. Criar o banco de dados

Executar o arquivo `database.sql` no MySQL.

### 3. Configurar acesso ao banco

Editar o arquivo `database.py` com seu usuário, senha e porta do MySQL.

### 4. Executar o sistema

```bash
python main.py
```