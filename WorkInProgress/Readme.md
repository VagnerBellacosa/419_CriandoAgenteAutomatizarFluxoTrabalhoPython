# 🤖 Criando um Agente para Automatizar um Fluxo de Trabalho em Python

## 📌 Descrição do Projeto

Este projeto tem como objetivo criar um Agente em Python capaz de interagir automaticamente com o Trello através de sua API REST.

O agente realiza operações de gerenciamento de tarefas, incluindo:

- Criação de cartões (Cards)
- Consulta de tarefas existentes
- Movimentação automática entre listas
- Automação de fluxo de trabalho
- Organização de atividades sem intervenção manual

O projeto demonstra conceitos fundamentais de:

- Automação de Processos
- Integração com APIs REST
- Uso de Variáveis de Ambiente
- Agentes Inteligentes
- Workflows Automatizados
- Gerenciamento de Tarefas

------

# 🎯 Objetivos do Desafio

Ao concluir este projeto será possível:

✅ Criar um ambiente Python isolado

✅ Consumir APIs REST

✅ Integrar aplicações externas

✅ Gerenciar tarefas automaticamente

✅ Utilizar credenciais de forma segura

✅ Construir a base para agentes inteligentes

------

# 🏗 Arquitetura da Solução

```text
+----------------+
| Usuário        |
+-------+--------+
        |
        v
+----------------+
| Agente Python  |
+-------+--------+
        |
        v
+----------------+
| API Trello     |
+-------+--------+
        |
        v
+----------------+
| Board Trello   |
+-------+--------+
        |
        v
+----------------+
| Cards/Listas   |
+----------------+
```

------

# 📋 Pré-Requisitos

Antes de iniciar o projeto, é necessário possuir:

## Python

Versão recomendada:

```text
Python 3.10+
```

Verificar instalação:

```bash
python --version
```

ou

```bash
python3 --version
```

------

## Conta no Trello

Criar conta gratuitamente:

[https://trello.com](https://trello.com/)

------

## Editor de Código

Sugestão:

- VS Code
- PyCharm
- IntelliJ IDEA

------

# 🔑 Configurando o Trello

## Passo 1 - Criar um Board

Exemplo:

```text
Projeto DIO
```

------

## Passo 2 - Criar Listas

```text
To Do

Doing

Done
```

------

## Passo 3 - Obter API Key

Acesse:

https://developer.atlassian.com/cloud/trello/

Gerar:

- API Key
- API Token

------

## Passo 4 - Obter IDs

Será necessário identificar:

```text
Board ID
Lista To Do ID
Lista Doing ID
Lista Done ID
```

Esses IDs serão utilizados nas chamadas da API.

------

# 📁 Estrutura do Projeto

```text
agente_trello/

│
├── app.py
├── trello.py
├── .env
├── requirements.txt
└── README.md
```

------

# 🐍 Criando Ambiente Virtual

## Windows

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

------

## Linux/Mac

```bash
python3 -m venv venv
```

Ativar:

```bash
source venv/bin/activate
```

------

# 📦 Instalando Dependências

Instalar bibliotecas:

```bash
pip install requests python-dotenv
```

------

# 📄 requirements.txt

```text
requests
python-dotenv
```

Instalação automática:

```bash
pip install -r requirements.txt
```

------

# 🔒 Configurando Variáveis de Ambiente

Criar arquivo:

```text
.env
```

Conteúdo:

```ini
TRELLO_KEY=SEU_KEY
TRELLO_TOKEN=SEU_TOKEN

BOARD_ID=XXXXXXXX

TODO_ID=XXXXXXXX
DOING_ID=XXXXXXXX
DONE_ID=XXXXXXXX
```

------

# 🔌 Testando Conexão com Trello

O primeiro teste do projeto consiste em validar a autenticação.

Fluxo:

```text
Python
   ↓
API Trello
   ↓
Usuário autenticado
```

Se a autenticação for bem-sucedida, a API retornará os dados da conta.

------

# 📝 Criando Cards

Função responsável por criar tarefas.

Exemplo:

```text
Nova tarefa:
"Estudar Agentes de IA"
```

Resultado:

```text
To Do

[ Estudar Agentes de IA ]
```

------

# 📚 Listando Cards

O agente consulta os cartões existentes.

Exemplo:

```text
To Do

[Estudar Python]

[Criar API]

[Documentar Projeto]
```

------

# 🔄 Movendo Cards

O agente pode alterar automaticamente o status da tarefa.

Fluxo:

```text
To Do
   ↓
Doing
   ↓
Done
```

------

# 🤖 Papel do Agente

O agente é responsável por:

1. Receber solicitações
2. Criar tarefas
3. Consultar tarefas
4. Atualizar status
5. Automatizar o fluxo

Fluxo completo:

```text
Solicitação
      ↓
Agente Python
      ↓
Cria Card
      ↓
Move para Doing
      ↓
Move para Done
      ↓
Concluído
```

------

# 🚀 Possíveis Melhorias

Após concluir o desafio, o projeto pode evoluir para:

## Integração com IA

Utilizando:

- OpenAI
- Ollama
- Gemini

Exemplo:

```text
Nova tarefa recebida
        ↓
IA analisa conteúdo
        ↓
Define prioridade
        ↓
Cria Card automaticamente
```

------

## Integração com E-mail

```text
E-mail recebido
       ↓
Agente interpreta
       ↓
Cria tarefa no Trello
```

------

## Integração com N8N

```text
Webhook
      ↓
N8N
      ↓
Agente Python
      ↓
Trello
```

------

# 🧪 Testes Recomendados

Executar os seguintes cenários:

### Teste 1

Criar Card

Resultado esperado:

```text
Card criado com sucesso
```

------

### Teste 2

Listar Cards

Resultado esperado:

```text
Lista de tarefas exibida
```

------

### Teste 3

Mover Card

Resultado esperado:

```text
Card movido para Doing
```

------

### Teste 4

Finalizar Card

Resultado esperado:

```text
Card movido para Done
```

------

# 📖 Conceitos Aprendidos

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Python
- APIs REST
- JSON
- HTTP
- Automação
- Agentes Inteligentes
- Variáveis de Ambiente
- Integração entre Sistemas
- Gestão de Tarefas
- Workflow Automation

------

# 🏆 Conclusão

Este projeto demonstra como construir um agente simples capaz de automatizar processos utilizando Python e Trello.

Embora seja um exemplo introdutório, a mesma arquitetura é utilizada em soluções corporativas para integração com sistemas como ServiceNow, Jira, Salesforce, SAP e até ambientes Mainframe, permitindo a criação de agentes cada vez mais inteligentes e autônomos.