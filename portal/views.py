#from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
#from django.template import Context, loader

def index(request):	
	template = loader.get_template("index.html")
	context = {
        'materia':'Tecnologias Web',
        'nombre':'Luis Ycaza',
    }

	return HttpResponse(template.render(context,request))

  