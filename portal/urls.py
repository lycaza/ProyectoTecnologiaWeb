from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('inicio', views.inicio, name='inicio'),
   
    #url(r'^path/to/url', TemplateView.as_view(template_name='paginas/index.html')),
]

