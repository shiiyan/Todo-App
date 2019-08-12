from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min
#from django.utils.dateformat import DateFormat
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from . models import ToDo, ToDoList
from . forms import ToDoListForm, ToDoForm, SearchForm, LoginForm

import datetime
from datetime import date


def login_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('index')
	else:
		messages.error(request, 'ユーザー名またはパスワードが間違っている！')
		return redirect('login')

def myloginpage(request):
	form = LoginForm()
	return render(request, 'todo/login.html', { 'form': form })

def logout_user(request):
	logout(request)
	return 

def index(request):
	todolists = ToDoList.objects.annotate(
		latest_todo_date=Max('todo__todo_create_date')
		).order_by('-latest_todo_date')
	form = ToDoListForm()

	for tdl in todolists:
		tdl.num_all = ToDo.objects.filter(todolist=tdl).count()
		tdl.num_completed = ToDo.objects.filter(
			todolist=tdl, complete=True
			).count()
		if (tdl.num_all) and (tdl.num_all > tdl.num_completed):
			tdl.latest_deadline = ToDo.objects.filter(
				todolist=tdl, complete=False
				).aggregate(Min('deadline'))['deadline__min']
		else:
			tdl.latest_deadline = date(2099,12,30)
		
		tdl.save()

	context = {
		'todolists': todolists,
		'form': form,

	}
	return render(request, 'todo/index.html', context)

def addTodolist(request):
	form = ToDoListForm(request.POST)
	if (form.is_valid()) &  (not ToDoList.objects.filter(todolist_text=request.POST['text']).exists()):
		messages.success(request, '新しいTodoリストが作成されました!')
		new_todolist = ToDoList(todolist_text=request.POST['text'])
		new_todolist.save()
		context = {
         	'new_todolist': new_todolist,
         	'form': form,

         }
		return render(request, 'todo/addtodolist.html', context)	
	elif ToDoList.objects.filter(todolist_text=request.POST['text']).exists():
		messages.error(request, 'Todoリストはすでに作成されています!')
	elif len(request.POST['text']) > 30:
		messages.error(request, 'Todoリストの名称は30文字以内にしてください!')
	elif len(request.POST['text']) < 1:
		messages.error(request, 'Todoリストの名称は1文字以上にしてください!')

	context = {
			'form': form,
		}
	return render(request, 'todo/addtodolist.html', context)

def detail(request, todolist_id):
	todolist = ToDoList.objects.get(pk=todolist_id)
	todolist.num_all = todolist.todo_set.count()
	todolist.num_completed = todolist.todo_set.filter(complete=True).count()
	
	form = ToDoForm()

	todos = todolist.todo_set.order_by('-id')

	context = {
		'todolist': todolist,
		'todos': todos,
		'form': form,

	}

	return render(request, 'todo/detail.html', context)

def addTodo(request, todolist_id):
	form = ToDoForm(request.POST)
	todolist = ToDoList.objects.get(pk=todolist_id)

	if (form.is_valid()) &  (not ToDo.objects.filter(todo_text=request.POST['text']).exists()):
		new_todo = ToDo(
			todolist=ToDoList.objects.get(pk=todolist_id),
			todo_text=request.POST['text'],
			deadline=request.POST['deadline'],
			)
		new_todo.save()

	elif ToDo.objects.filter(todo_text=request.POST['text']).exists():
		messages.error(request, 'Todoはすでに作成されています!')
	elif len(request.POST['text']) > 30:
		messages.error(request, 'Todoの名称は30文字以内にしてください!')
	elif len(request.POST['text']) < 1:
		messages.error(request, 'Todoの名称は1文字以上にしてください!')

	return HttpResponseRedirect(reverse('detail', args=(todolist.id,)))

def completeTodo(request, todo_id, todolist_id):
	todolist = ToDoList.objects.get(pk=todolist_id)
	todo = ToDo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return HttpResponseRedirect(reverse('detail', args=(todolist.id,)))

def uncompleteTodo(request, todo_id, todolist_id):
	todolist = ToDoList.objects.get(pk=todolist_id)
	todo = ToDo.objects.get(pk=todo_id)
	todo.complete = False
	todo.save()

	return HttpResponseRedirect(reverse('detail', args=(todolist.id,)))

def searchpage(request):
	form = SearchForm()

	context = {
		'form': form,
	}

	return render(request, 'todo/search.html', context)

def result(request):
	form = SearchForm(request.POST)

	if form.is_valid():
		todolists=ToDoList.objects.filter(todolist_text__icontains=request.POST['text']).order_by('-list_create_date')
		todos=ToDo.objects.filter(todo_text__icontains=request.POST['text']).order_by('-todo_create_date')
		todolist_count=len(todolists)
		todo_count=len(todos)

	context = {
		'form': form,
		'todolists': todolists,
		'todos': todos,
		'todolist_count': todolist_count,
		'todo_count': todo_count,
	}

	return render(request, 'todo/result.html', context)

def deleteTodolist(request, todolist_id):
	ToDoList.objects.filter(id__exact=todolist_id).delete()

	return redirect('index')

def deletecompleted(request, todolist_id):
	todolist = ToDoList.objects.get(pk=todolist_id)
	todolist.todo_set.filter(complete__exact=True).delete()

	return HttpResponseRedirect(reverse('detail', args=(todolist.id,)))




















