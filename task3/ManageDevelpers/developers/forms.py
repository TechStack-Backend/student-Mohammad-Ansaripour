from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    developers = forms.ModelMultipleChoiceField(
        queryset=DevelopersModel.objects.all(),
        widget=forms.CheckboxSelectMultiple, 
        required=True)
    class Meta:
        model= ProjectModel
        fields=[
            "title",
            "description",
            "developers"
        ]
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        queryset = ProjectModel.objects.filter(title=title)

        if self.instance.pk:  
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise forms.ValidationError("titel is in used")
        return title
    



class DevelopersForms(forms.ModelForm):
    class Meta:
        model= DevelopersModel
        fields=[
            "first_name",
            "last_name",
            "email",
            "username",
            "age",
        ]
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("username is required")
        if DevelopersModel.objects.filter(username=username).exists():
            raise forms.ValidationError("this username already in use.")
        
        return username

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillsModel
        fields = ["title","desciption"]



# SkillFormSet = forms.inlineformset_factory(
#     DevelopersModel,
#     SkillsModel,
#     form=SkillForm,
#     extra=1,        
#     can_delete=True 
# )
