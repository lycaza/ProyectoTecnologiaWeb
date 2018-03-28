# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
#from django.template import Context, loader
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):	
	template = loader.get_template("index.html")	
	return HttpResponse(template.render())


def login(request):	
	template = loader.get_template("login.html")	
	return HttpResponse(template.render())

@csrf_exempt
def autentica(request):
	
	username = request.POST['usuario']
	clave = request.POST['clave']
	print(username)
	print(clave)

	#return render(request, 'inicio.html', {'form':form})
	template = loader.get_template("inicio.html")	
	return HttpResponse(template.render())