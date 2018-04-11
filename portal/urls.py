from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),    
    path('logout', views.logout, name='logout'),
    path('autentica', views.autentica, name='autentica'),
   	path('principal', views.principal, name='principal'),
   	path('ventas_agencias', views.ventas_agencias, name='ventas_agencias'),
   	path('indicador', views.indicador, name='indicador'), 
	  path('obtener_clientes', views.obtener_clientes, name='obtener_clientes'),     	
   	path('indicador', views.indicador, name='indicador'),   	
	  path('indicador_2', views.indicador_2, name='indicador_2'),  
   	path('ventas_categorias', views.ventas_categorias, name='ventas_categorias'),
   	path('obtener_agencias', views.obtener_agencias, name='obtener_agencias'),   
   	path('actual_estimado_categorias', views.actual_estimado_categorias, name='actual_estimado_categorias'), 
    path('obtener_lista_categorias', views.obtener_lista_categorias, name='obtener_lista_categorias'),         
]

