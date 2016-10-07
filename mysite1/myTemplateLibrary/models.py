# coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 100)
	author =  models.CharField(max_length=10)
	def __str__(self):
		return self.title
