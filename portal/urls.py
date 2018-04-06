from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),    
    path('autentica', views.autentica, name='autentica'),
   	path('principal', views.principal, name='principal'),
   	path('ventas_agencias', views.ventas_agencias, name='ventas_agencias'),
<<<<<<< HEAD
   	path('indicador', views.indicador, name='indicador'), 
	path('obtener_clientes', views.obtener_clientes, name='obtener_clientes'),     	
=======
   	path('indicador', views.indicador, name='indicador'),   	
	path('indicador_2', views.indicador_2, name='indicador_2'),  
>>>>>>> 0eda2c538def9493a2e6111fc395cc208ec3a799
   	path('ventas_categorias', views.ventas_categorias, name='ventas_categorias'),
   	path('obtener_agencias', views.obtener_agencias, name='obtener_agencias'),   
    #url(r'^path/to/url', TemplateView.as_view(template_name='paginas/index.html')),
]

