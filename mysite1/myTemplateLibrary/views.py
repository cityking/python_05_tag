from django.shortcuts import render

# Create your views here.
def hello(request):
	hello = "Hello WorlD"
	return render(request, 'now.html', locals())
	
