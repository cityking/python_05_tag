# encoding: utf-8
from django.contrib import admin
from myTemplateLibrary.models import Book
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Register your models here.
admin.site.register(Book)

