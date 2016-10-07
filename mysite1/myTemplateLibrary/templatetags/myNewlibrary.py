# coding: utf-8
from django import template

#创建全局变量register，用来注册你的自定义标签和过滤器
register = template.Library()


#定义过滤器函数
#def remove(var, arg):
#	#移除var中的arg字符串
#	return var.replace(arg, '')
#
#def lower(value):
#	return value.lower()


#注册过滤器函数
#register.filter('remove', remove)
#register.filter('lower', lower)


#使用装饰器
@register.filter(name='remove')
def remove(var, arg):
	#移除var中的arg字符串
	return var.replace(arg, '')

@register.filter
def lower(value):
	return value.lower()


#定义Node节点类，实现render方法
import datetime
class CurrentTimeNode(template.Node):
	def __init__(self, format_string):
		self.format_string = str(format_string)
	def render(self, context):
		now = datetime.datetime.now()
		context['current_time'] = now.strftime(self.format_string)

		return "" 
class CurrentTimeNode2(template.Node):
	def __init__(self, format_string, var_name):
		self.format_string = str(format_string)
		self.var_name = var_name
	def render(self, context):
		now = datetime.datetime.now()
		context[self.var_name] = now.strftime(self.format_string)

		return "" 

#创建compilation函数用于获取模板中的参数并创建相应的Node类对象
	#@register.tag(name='current_time')
#def do_current_time(parser, token):
#	try:
#		tag_name, format_string = token.split_contents()
#	except ValueError:
#		msg = '%r tag requires a single argument' % token.split_contents()[0]
#		raise template.TemplateSyntaxError(msg)
#	return CurrentTimeNode(format_string[1:-1])
	

def do_current_time(parser, token):
	try:
		tag_name, args = token.contents.split(None, 1)
	except ValueError:
		msg = '%r tag requires a single argument' % token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	import re
	m = re.search(r'(.*?) as (\w+)', args)
	if m:
		format_string, var_name = m.groups()
	else:
		msg = "%r tag has invalid arguments" % tag_name
		raise template.TemplateSyntaxError(msg)
	if not (format_string[0] == format_string[-1] and format_string[0] in ("'",'"')):
		msg = "%r tag's argument should be in quotes" % tag_name
		raise template.TemplateSyntaxError(msg)
		
	return CurrentTimeNode2(format_string[1:-1], var_name)
def do_current_time2(parser, token):
	try:
		args = token.split_contents()
		if len(args)==4 and args[-2] == 'as':
			var_name = args[-1]
			format_string = args[1]
		elif len(args)!=2:
			raise template.TemplateSyntaxError('Invalid arguments')
	except ValueError:
		msg = '%r tag requires a single argument' % token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	
	return CurrentTimeNode2(format_string[1:-1], var_name)

#注册tag
register.tag('current_time', do_current_time2)

def get_current_time(format_string):
	return datetime.datetime.now().strftime(str(format_string))
#register.simple_tag(get_current_time)
register.assignment_tag(get_current_time)
