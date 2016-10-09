# coding: utf-8
from __future__ import absolute_import
from jinja2 import Environment

def environment(**options):
	env = Environment(**options)
	env.filters['my_lower']=lower
	return env

#自定义过滤器
def lower(value):
	return value.lower()
	
