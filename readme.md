💰 API de Controle Financeiro

API REST para gerenciamento de finanças pessoais, desenvolvida com FastAPI, focada em organização de receitas, despesas e geração de resumos financeiros mensais.

📌 Sobre o Projeto

Este projeto tem como objetivo fornecer uma API simples, organizada e escalável para controle financeiro pessoal, permitindo:

Cadastro e autenticação de usuários

Registro de receitas e despesas

Filtros por mês e ano

Resumo financeiro mensal

Estrutura preparada para crescimento (boas práticas com schemas, separação de camadas e regras de negócio)

🚀 Tecnologias Utilizadas

Python 3.12+

FastAPI

SQLAlchemy

SQLite (ambiente de desenvolvimento)

Pydantic

Uvicorn

Autenticação com JWT

📂 Estrutura do Projeto
controle_financeiro/
│
├── app/
│   ├── core/          # Configurações, segurança (JWT), dependências
│   ├── models/        # Modelos do banco (SQLAlchemy)
│   ├── schemas/       # Schemas de entrada e saída (Pydantic)
│   ├── services/      # Regras de negócio
│   ├── routes/        # Rotas da aplicação
│   ├── database.py    # Conexão com banco
│   └── main.py        # Inicialização da aplicação
│
├── requirements.txt
└── README.md
⚙️ Instalação e Execução
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/controle-financeiro.git
cd controle-financeiro
2️⃣ Criar e ativar ambiente virtual
python -m venv env
Linux / Mac:
source env/bin/activate
Windows:
env\Scripts\activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Executar o servidor
uvicorn app.main:app --reload

Acesse a documentação interativa em:

http://127.0.0.1:8000/docs
🔐 Autenticação

A API utiliza autenticação baseada em JWT.

Fluxo básico:

Registrar usuário

Realizar login

Receber token JWT

Enviar token no header:

Authorization: Bearer seu_token_aqui
📊 Funcionalidades Principais
👤 Usuários

Registro

Login

Proteção de rotas autenticadas

💸 Transações

Criar receita

Criar despesa

Listar transações

Filtrar por mês e ano

Atualizar transações

Deletar transações

📈 Resumo Financeiro

Total de receitas

Total de despesas

Saldo mensal

Filtro por período

🧠 Regras de Negócio Implementadas

Cada usuário só pode visualizar suas próprias transações

Separação entre camada de rota e camada de serviço

Schemas de entrada e saída separados

Validações com Pydantic

Filtro por mês/ano usando funções apropriadas do banco

🛠 Possíveis Melhorias Futuras

Paginação

Categorias de transações

Metas financeiras

Relatórios em PDF

Deploy em produção (Docker + PostgreSQL)

Integração com frontend (React)

🧪 Testes (Sugestão)

Você pode utilizar:

Pytest

HTTPX

TestClient do FastAPI

📖 Documentação Automática

A documentação é gerada automaticamente pelo FastAPI:

Swagger: /docs

Redoc: /redoc

👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática de arquitetura de APIs modernas com FastAPI.