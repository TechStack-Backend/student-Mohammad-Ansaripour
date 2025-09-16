from django.contrib import admin
from django.urls import path
from . import views

app_name="developers"

urlpatterns=[
    path("developers/",views.developersList,name="developers_list"),
    path("developers/<str:username>/",views.developersDetails,name="developers_detail"),
    path("projects/",views.projectsList,name="projects_list"),
    path("projects/<int:id>/",views.projectsDetails,name="projects_detail"),

]
