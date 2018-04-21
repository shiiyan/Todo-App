from django.contrib import admin
from . models import ToDo, ToDoList

# Register your models here.
admin.site.register([ToDo,ToDoList])
