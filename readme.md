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

### Realizar migrações iniciais e criar super usuario

- Migrar apps principais para o funcionamento correto do django. São responsáveis por configurar as tabelas essenciais para o funcionamento do framework. Autenticação, sessões, admin.

- python manage.py migrate

        ```
        Operations to perform:
            Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
            Applying contenttypes.0001_initial... OK
            Applying auth.0001_initial... OK
            Applying admin.0001_initial... OK
            Applying admin.0002_logentry_remove_auto_add... OK
            Applying admin.0003_logentry_add_action_flag_choices... OK
            Applying contenttypes.0002_remove_content_type_name... OK
            Applying auth.0002_alter_permission_name_max_length... OK
            Applying auth.0003_alter_user_email_max_length... OK
            Applying auth.0004_alter_user_username_opts... OK
            Applying auth.0005_alter_user_last_login_null... OK
            Applying auth.0006_require_contenttypes_0002... OK
            Applying auth.0007_alter_validators_add_error_messages... OK
            Applying auth.0008_alter_user_username_max_length... OK
            Applying auth.0009_alter_user_last_name_max_length... OK
            Applying auth.0010_alter_group_name_max_length... OK
            Applying auth.0011_update_proxy_permissions... OK
            Applying auth.0012_alter_user_first_name_max_length... OK
            Applying sessions.0001_initial... OK
        ```

- python manage.py createsuperuser

### Criar models

- task/models.py
- importante configurar (settings.py) para caso usar informações do models como campas de data.

    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

- Realizar as migrações
        ```
        python manage.py makemigrations
        python manage.py migrate
        ```
- Configurar o metodo __str__ para personalizar a saída de com um nome mais legivel na admin do django. Se não definir, o Django usará um nome genérico (Task object (id)).
        ```
        def __str__(self):
            return f'{self.title}'
        ```

### Registrar models criados na area administrativa

- Registrar model na admin.py. Permite configurar meu model pela admin do django. Decorator @admin.register(models.Task) registra e referencia qual model estou administrando. Padronizar o nome da classe com a mesma classe do model e colocar Admin no nome.

        ``` 
        @admin.register(models.Task)
        class taskAdmin(admin.ModelAdmin):
            ...
        ```

<!-- ###  -->
<!-- pendencias - campo datefield no models.py -->

### Criar pasta de views

- Criar uma pasta de views pra organizar as views, de fato vao ter muitas view e para organizar em uma pasta só, pode 'burlar' o django para ele usar uma package views e ler o init primeiro para importar tudo da nova view criada.

- IMPORTANTE: Não esquecer de importar tudo do arquivo dentro do init


- index.html criado o bloco e usando css ja existente. 
- atualizar a view pra rendereizar um novo contexto 
def index(request):
    
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
    }
    
    return render(
        request,
        'task/index.html',
        context,
    )

- 