#from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
#from django.template import Context, loader

def index(request):	
	template = loader.get_template("index.html")
	
	return HttpResponse(template.render())


def login(request):	
	template = loader.get_template("login.html")
	
	return HttpResponse(template.render())


def inicio(request):	
	template = loader.get_template("inicio.html")
	
	return HttpResponse(template.render())

  