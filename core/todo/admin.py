from csv import list_dialects
from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('Description', 'user', 'created_date', 'done')

admin.site.register(Task, TaskAdmin)