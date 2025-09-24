from django.contrib import admin
from django.urls import path
from . import views

app_name="developers"

urlpatterns=[
    path("developers/",views.developersList,name="developers_list"),
    path("developers/add/",views.DeveloperCreativeView.as_view(),name="developer_create"),
    path("developers/<str:username>/",views.developersDetails,name="developers_detail"),
    path("projects/",views.projectsList,name="projects_list"),
    path("projects/add/",views.projectCreate,name="projects_create"),
    path("projects/<int:id>/",views.projectsDetails,name="projects_detail"),
]
