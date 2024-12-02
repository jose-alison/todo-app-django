# To-Do App

![Python Version](https://img.shields.io/badge/Python->=3.12-blue) ![GitHub License](https://img.shields.io/github/license/jose-alison/todo-app-django) ![Release](https://img.shields.io/github/v/tag/jose-alison/todo-app-django)


Este é um aplicativo de lista de tarefas desenvolvido usando Django. Ele permite que os usuários criem, visualizem, editem e excluam tarefas.

## Funcionalidades

- Adicionar novas tarefas
- Visualizar todas as tarefas
- Editar tarefas existentes
- Excluir tarefas

## Tecnologias Utilizadas

- Django
- UV
- SQLite (banco de dados padrão do Django)
- HTML/CSS para o front-end
- Tailwind CSS

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/jose-alison/todo-app-django.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd app
    ```
3. Instale a biblioteca UV:
    ```bash
    pip install uv
    ```
4. Crie um ambiente com UV:
    ```bash
    uv sync
    ```
5. Aplique as migrações do banco de dados:
    ```bash
    uv run manage.py migrate
    ```
6. Inicie o servidor de desenvolvimento:
    ```bash
    uv run manage.py runserver
    ```

## Uso

1. Acesse o aplicativo no navegador:
    ```
    http://127.0.0.1:8000/
    ```
2. Use a interface para adicionar, visualizar, editar e excluir tarefas.

## Contribuição

1. Faça um fork do projeto
2. Crie uma nova branch:
    ```bash
    git checkout -b minha-nova-funcionalidade
    ```
3. Faça suas alterações e commit:
    ```bash
    git commit -m 'Adiciona nova funcionalidade'
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin minha-nova-funcionalidade
    ```
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/jose-alison/todo-app-django/blob/main/LICENSE) para mais detalhes.

