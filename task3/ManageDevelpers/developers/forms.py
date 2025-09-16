from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model= ProjectModel
        fielde=[
            "title",
            "description"
        ]

class DevelopersForm(forms.Form):

    f_name=forms.CharField(max_length=50,required=True)
    l_name=forms.CharField(max_length=75,required=True)
    email=forms.EmailField(required=True)
    ege=forms.IntegerField(max_value=150,min_value=0)
