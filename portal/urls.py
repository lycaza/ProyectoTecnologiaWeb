from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),    
    path('autentica', views.autentica, name='autentica'),
   	path('principal', views.principal, name='principal'),   	
    #url(r'^path/to/url', TemplateView.as_view(template_name='paginas/index.html')),
]

