# Projeto Django: Sistema de cadastro e gerenciamento de alunos, com funcionalidades de CRUD: criar, listar, editar, detalhar, desativar e excluir alunos.

## Tecnologias utilizadas
- Python 3.11
- Django 5.2.4
- Bootstrap 5 (front-end)
- SQLite (banco de dados padrão do Django)

## Instalação

1. **Clonar o repositório**
- git clone https://github.com/hwtcp/matricula2bim.git
- cd matricula2bim
2. **Criar e ativar um ambiente virtual**
  No windows:
- python -m venv venv
- venv\Scripts\activate
  No Linux:
- python3 -m venv venv
- source venv/bin/activate
3. **Instalar dependências**
- pip install -r requirements.txt
4. **Configurar o projeto**
  Aplicar migrações:
- python manage.py makemigrations
- python manage.py migrate

## Execução

1. **Executar o projeto**
- python manage.py runserver
2. **Funcionalidades**
- Funcionalidades
- Cadastro de alunos com dados pessoais, endereço e informações acadêmicas
- Listagem de alunos cadastrados
- Edição de alunos
- Detalhes completos do aluno
- Desativar / Ativar aluno
- Excluir aluno





