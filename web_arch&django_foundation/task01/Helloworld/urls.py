from django.urls import path
from . import views


app_name="helloworld"
urlpatterns=[
    path("index/",views.indexView,name='index')
]