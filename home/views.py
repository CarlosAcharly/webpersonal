from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request):
    name = 'Carlos Hernandez'
    career='Software Developer'
    context = {
        "name": name,
        "career": career
    }
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def projects(request):
    projects=Project.objects.all().order_by('id')[:5]
    context = {
        "projects": projects
    }
    return render(request, 'home/projects.html', context)

def about(request):
    name='Carlos hernandez'
    description='Nacido en... lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe nostrum ullam eveniet pariatur voluptates odit, fuga atque ea nobis sit soluta odio.</p>'
    context = {
        "name": name,
        "description": description
    }
    return render(request, 'home/about.html',context)
