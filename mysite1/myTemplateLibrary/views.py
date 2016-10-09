from django.shortcuts import render

# Create your views here.
def hello(request):
	hello = "Hello WorlD"
	return render(request, 'now.html', locals())
def home(request):
	return render(request, 'home.html', {'tempValue':[1,2,3]})
	
