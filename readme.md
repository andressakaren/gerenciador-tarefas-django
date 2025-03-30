- app criado adicionar nos settings.py 
INSTALLED_APPS = [
    'task',

    
]

- infos
git status - lista as mudanças que vao ser comitadas

- criar base_static e base_templates, pra manter consistencia em todo o site no sentido de design. 
- criar pasta global (pra ter um namespacing)
- lembrar q n é do djnago e tem q configurar nos settings. 
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                BASE_DIR / 'base_templates',
            ],
    STATICFILES_DIRS = (
        BASE_DIR / 'base_static',
    )

-criar templates dentro do app (task) com um namespacing task, index.html é a home do nosso app
