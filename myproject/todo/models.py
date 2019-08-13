import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	stress_point = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

class ToDoList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	todolist_text = models.CharField(max_length=60) #Todoリストの名称は30文字以内にしてください。
	list_create_date = models.DateField('date created', default=datetime.date.today)
	num_all = models.IntegerField(default=0)
	num_completed = models.IntegerField(default=0)
	latest_deadline = models.DateField('latest deadline',default=datetime.date(2099,12,30))

	def __str__(self):
		return self.todolist_text

class ToDo(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	todo_text = models.CharField(max_length=60) #Todoの名称は30文字以内にしてください。
	deadline = models.DateField('deadline')
	todo_create_date = models.DateField('date created', default=datetime.date.today)
	complete = models.BooleanField(default=False)
	
	def __str__(self):
		return self.todo_text


