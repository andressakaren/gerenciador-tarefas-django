from django.contrib import admin
from task import models

@admin.register(models.Task)
class taskAdmin(admin.ModelAdmin):
    list_display = 'id','title', 'deadline_date', 'description',
    ordering = '-id',
    # list_filter - pra ver por status 
    search_fields = 'title', #colocar o usuario
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'title', 'deadline_date',