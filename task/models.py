from django.db import models
from django.contrib.auth.models import User

# Filtros por usuário, status e data de vencimento.

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
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas_criadas', blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='atribuido_a', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
