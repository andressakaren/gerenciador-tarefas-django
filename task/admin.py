from django.contrib import admin
from task import models

@admin.register(models.Task)
class taskAdmin(admin.ModelAdmin):
    list_display = 'id','title', 'status', 'deadline_date', 'description', 'created_by', 'assigned_to',
    ordering = '-id',
    # list_filter - pra ver por status 
    search_fields = 'title', 'created_by',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'title', 'deadline_date', 'status',
    
@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'email',
    ordering = 'id',
    list_per_page = 10
    list_max_show_all = 100
    list_editable =  'name',