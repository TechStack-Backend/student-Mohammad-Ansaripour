from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def devListView(request):
    developers=DevelopersModel.objects.all()
    context={
        "developers":developers,
    }
    return render(request,"developersInfo/developers_list.html",context=context)


def devDetailView(request,username):
    developer=get_object_or_404(DevelopersModel,username=username)
    context={
        "fname":developer.first_name,
        "lname":developer.last_name,
        "username":developer.username,
        "skills":developer.skills,
    }
    return render(request,"developersInfo/developers_cv.html",context=context)
