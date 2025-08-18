from django.urls import path
from . import views


app_name="DevInfoApp"
urlpatterns=[
    path("developers/",views.devListView,name="developersList"),

]