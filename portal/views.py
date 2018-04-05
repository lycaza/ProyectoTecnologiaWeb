# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from portal.dao import *
from django.http import HttpResponseRedirect

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
		
	conn = create_connection('proyecto.sqlite3')
	if verifica(conn,username,clave):
		return HttpResponseRedirect("principal")		
	else:
		print("error")
	conn.close()
	#return render(request, 'inicio.html', {'form':form})		

def principal(request):	
	template = loader.get_template("principal.html")	
	return HttpResponse(template.render())

def ventas_agencias(request):	
	conn = create_connection('proyecto.sqlite3')
	data= obtener_ventas_agencias(conn)	
	conn.close()

	return HttpResponse(data)

def indicador(request):	
	agencia = request.GET['agencia']

	conn = create_connection('proyecto.sqlite3')
	porcentaje= obtener_indicador(conn,agencia)	
	conn.close()

	return HttpResponse(porcentaje)

def ventas_categorias(request):	
	conn = create_connection('proyecto.sqlite3')
	data= obtener_ventas_categorias(conn)	
	conn.close()

	return HttpResponse(data)

def obtener_agencias(request):	
	conn = create_connection('proyecto.sqlite3')
	data= obtener_lista_agencias(conn)	
	conn.close()

	return HttpResponse(data)