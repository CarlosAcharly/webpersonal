from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
    name = 'Agrofeed System'
    career='Ingenieria en sistemas computacionales'
    context = {
        "name": name,
        "career": career
    }
    return render(request, 'home/index.html', context)

def contact(request):
    name='Agrofeed System'
    context={
        "name": name
    }
    return render(request, 'home/contact.html', context)

def projects(request):
    name='Agrofeed System'
    projects=Project.objects.all().order_by('id')[:5]
    context = {
        "name": name,
        "projects": projects
    }
    return render(request, 'home/projects.html', context)

def about(request):
    name='Agrofeed System'
    description='Nacido en... lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit soluta odio.</p>'
    context = {
        "name": name,
        "description": description
    }
    return render(request, 'home/about.html',context)

def products_view(request):
    projects = [
        {
            "name": "Producto 1",
            "image": "img/avatar.jpg",
            "short_description": "Descripción corta del Producto 1",
            "description": "Descripción detallada del Producto 1.",
            "url": None
        },
        {
            "name": "Producto 2",
            "image": "img/lechones.jpg",
            "short_description": "Descripción corta del Producto 2",
            "description": "Descripción detallada del Producto 2.",
            "url": None
        },
    ]
    return render(request, 'products.html', {'projects': projects})