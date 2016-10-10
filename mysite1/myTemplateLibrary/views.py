# coding: utf-8
from django.shortcuts import render
from models import ToDo

# Create your views here.
def hello(request):
	hello = "Hello WorlD"
	return render(request, 'now.html', locals())
def home(request):
	return render(request, 'home.html', {'tempValue':[1,2,3]})
def todoList(request):
	return render(request, 'todo.html', {'showtype':'未完成事件', 'todoList':ToDo.objects.incomplete().high()})
