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
#创建compilation函数用于获取模板中的参数并创建相应的Node类对象
	#@register.tag(name='current_time')
def do_current_time(parser, token):
	try:
		tag_name, format_string = token.split_contents()
	except ValueError:
		msg = '%r tag requires a single argument' % token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	return CurrentTimeNode(format_string[1:-1])
	
#注册tag
register.tag('current_time', do_current_time)
