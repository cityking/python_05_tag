# coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 100)
	author =  models.CharField(max_length=10)
	def __str__(self):
		return self.title

class IncompleteTodoManager(models.Manager):
	def get_queryset(self):
		return super(IncompleteTodoManager, self).get_queryset().filter(is_done=False)

class HighPriorityTodoManager(models.Manager):
	def get_queryset(self):
		return super(HighPriorityTodoManager, self).get_queryset().filter(priority=1)

class TodoManager(models.Manager):
	def Incomplete(self):
		return self.filter(is_done=False)
	
	def high(self):
		return self.filter(priority=1)

class TodoQueryset(models.QuerySet):
	def Incomplete(self):
		return self.filter(is_done=False)
	
	def high(self):
		return self.filter(priority=1)

class NewTodoManager(models.Manager):
	def get_queryset(self):
		return TodoQueryset(self.model, using=self._db)
	
	def incomplete(self):
		return self.get_queryset().Incomplete()
	
	def high(self):
		return self.get_queryset().high()

class ToDo(models.Model):
	content = models.CharField(max_length = 200)
	is_done = models.BooleanField(default = False)
	priority = models.IntegerField(default=1)

	def __str__(self):
		return "%s-%d" %(self.content, self.priority)
	incomplete = IncompleteTodoManager()
	highpriority = HighPriorityTodoManager()
	#objects = TodoQueryset.as_manager()
	objects = NewTodoManager()
