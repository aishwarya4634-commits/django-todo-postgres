from django.contrib import admin
from .models import TodoList, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Task)
