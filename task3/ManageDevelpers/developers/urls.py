from django.contrib import admin
from django.urls import path
from . import views

app_name="developers"

urlpatterns=[
    path("developers/",views.DevelopersList.as_view(),name="developers_list"),
    path("developers/add/",views.DeveloperCreativeView.as_view(),name="developer_create"),
    path("developers/<str:username>/",views.DeveloperDetails.as_view(),name="developers_detail"),
    path("developers/update/<str:username>/",views.DeveloperUpdateView.as_view(),name="developers_update"),
    path("developers/delete/<str:username>/",views.DeveloperDeleteView.as_view(),name="developers_delete"),
    path("projects/",views.ProjectListView.as_view(),name="projects_list"),
    path("projects/<int:id>/",views.ProjectDetailView.as_view(),name="projects_detail"),
    path("projects/add/",views.projectCreate,name="projects_create"),
    path("projects/update/<int:id>/",views.ProjectUpdataView.as_view(),name="projects_update"),
    path("projects/delete/<int:id>/",views.ProjectDeleteView.as_view(),name="projects_delete"),
]
