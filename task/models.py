from django.db import models

# Usuários
# nome e e-mail únicos.

# Tarefas
# título, descrição, data de vencimento e status (pendente, em andamento, concluída).

# Filtros por usuário, status e data de vencimento.

class CustomUser(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, unique=True)
    
    def __str__(self):
        return f'{self.name}'

class Task(models.Model):
    # ID - Primary key é criada automaticamente pelo django
    STATUS = [
        ('pendente', 'Pendente'),
        ('em andamento', 'Em andamento'),
        ('concluída', 'Concluída'),
    ]
    
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    deadline_date = models.DateField() # N SEI SE É ASSIM
    status = models.CharField(max_length=13, choices=STATUS, default='pendente') 
    
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tarefas_criadas', blank=True, null=True)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='atribuido_a', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
