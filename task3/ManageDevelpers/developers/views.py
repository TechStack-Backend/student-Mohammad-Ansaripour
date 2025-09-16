from django.shortcuts import render,get_object_or_404
from .models import *

def developersList(request):
    developers=DevelopersModel.objects.all()
    context={
        "developers":developers,
        }
    return render(request,"developers/developersList.html",context)

def developersDetails(request,username):
    developer=get_object_or_404(DevelopersModel,username=username)
    context={
        "developer":developer
    }
    return render(request,"developers/developerDetailes.html")
def developerCreate(request):
    pass




def projectsList(request):
    projects=ProjectModel.objects.all()
    context={
        "projects":projects
    }
    return render(request,"developers/projectsLis.html",context)

def projectsDetails(request,id):
    project=get_object_or_404(ProjectModel,id=id)
    context={
        "project":project
    }
    return render(request,"developers/projectsDetails.html",context)

def projectCreat(requests):
    pass
