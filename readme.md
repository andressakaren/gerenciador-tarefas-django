# Iniciar o projeto Django

    ```
    python -m venv venv
    . venv/bin/activate
    pip install django
    django-admin startproject project .
    python manage.py startapp task
    python manage.py runserver
    ```

## Configurar o git

    ```
    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main
    # Configure o .gitignore
    git init
    git add .
    git commit -m 'Mensagem'
    git remote add origin URL_DO_GIT
    git status - lista as mudanças que vao ser comitadas
    ```

## Migrando a base de dados do Django

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

## Criando e modificando a senha de um super usuário Django

    ```
    python manage.py createsuperuser
    python manage.py changepassword USERNAME
    ```

## Etapas

### Criar app - task

- python manage.py startapp task
    Depois de criar o app, verificar o nome em task/apps.py, adicionar nos settings.py do project.

        ```
            INSTALLED_APPS = [
                'task',
            ]
        ```

### Criar pastas bases

- criar base_static e base_templates: pra manter consistencia em todo o site.

- base_templates/
  - global (namespace)/
    - base.html
- base_static/
  - global (namespace)/
    - css/
      - style.css

- Configurar nos settings.py, pois não são pastas padrão do django.

        ```
            TEMPLATES = [
                {
                    'DIRS': [
                        BASE_DIR / 'base_templates',
                    ],
                }
            ]
            ...
            STATICFILES_DIRS = (
                BASE_DIR / 'base_static',
            )
        ```

### Criar pasta templates dentro do app

- Criar templates dentro do app (task) com um namespacing task, index.html é a home do nosso app.
