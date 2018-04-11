# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from portal.dao import *
from django.http import HttpResponseRedirect

def index(request):	
	template = loader.get_template("index.html")	
	return HttpResponse(template.render())


def login(request):	
	template = loader.get_template("login.html")	
	return HttpResponse(template.render())

def logout(request):	
	request.session['usuario']= ""
	request.session['clave']= ""
	return HttpResponseRedirect("login")

@csrf_exempt
def autentica(request):	
	username = request.POST['usuario']
	clave = request.POST['clave']

	conn = create_connection('proyecto.sqlite3')
	if verifica(conn,username,clave):
		request.session['usuario']= username
		request.session['clave']= clave
		return HttpResponseRedirect("principal")		
	else:
		return HttpResponse("<h4>Error de autenticaci&oacute;n!</h4> <a href='login'>[Regresar]</a>")
	conn.close()
		

def principal(request):	
	if request.session['usuario']!="":
		template = loader.get_template("principal.html")	
		return HttpResponse(template.render())
	else:
		return HttpResponse("<h4>No hay sesiones activas!</h4> <a href='login'>[Regresar]</a>")

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
	
def indicador_2(request):	
	agencia = request.GET['agencia']

	conn = create_connection('proyecto.sqlite3')
	porcentaje_2= obtener_indicador_2(conn,agencia)	
	print(porcentaje_2)
	conn.close()
	
	return HttpResponse(porcentaje_2)

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

def actual_estimado_categorias(request):	
	agencia = request.GET['agencia']
	conn = create_connection('proyecto.sqlite3')
	data= obtener_actual_estimado_categorias(conn,agencia)	
	conn.close()

	return HttpResponse(data)
	
def obtener_clientes(request):	
	agencia = request.GET['agencia']
	
	conn = create_connection('proyecto.sqlite3')
	data= obtener_lista_clientes(conn,agencia)	
	conn.close()

	return HttpResponse(data)

def obtener_lista_categorias(request):	
	conn = create_connection('proyecto.sqlite3')
	data= obtener_ventas_categorias(conn)	
	conn.close()

	return HttpResponse(data)