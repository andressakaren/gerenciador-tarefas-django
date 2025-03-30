from django.db import models

# Usuários
# nome e e-mail únicos.

# Tarefas
# título, descrição, data de vencimento e status (pendente, em andamento, concluída).

# Filtros por usuário, status e data de vencimento.

class Task(models.Model):
    # ID - Primary key é criada automaticamente pelo django
    STATUS = [
        ('pendente', 'Pendente'),
        ('em andamento', 'Em andamento'),
        ('concluída', 'Concluída'),
    ]
    
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True) # blank=True -- Pode deixar sem preencher
    deadline_date = models.DateField() # N SEI SE É ASSIM
    status = models.CharField(max_length=13, choices=STATUS, default='pendente') # N SEI SE É ASSIM
    
    def __str__(self):
        return f'{self.title}'
