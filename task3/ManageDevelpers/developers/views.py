from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy


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
    return render(request,"developers/developersDetails.html",context)

class DeveloperCreativeView(CreateView):
    model=DevelopersModel
    template_name="forms/developers_create_form.html"
    form_class= forms.DevelopersForms
    # success_url="/developers/"

    def get(self, request):
        dev_form = forms.DevelopersForms()
        skill_form = forms.SkillForm()
        return render(request, self.template_name, {
            'dev_form': dev_form,
            'skill_form': skill_form
        })
        
    def post(self, request, *args, **kwargs):
        dev_form=forms.DevelopersForms(request.POST)
        skill_form=forms.SkillForm(request.POST)
        if dev_form.is_valid() and skill_form.is_valid():
            developer=dev_form.save()
            skill=skill_form.save(commit=False)
            skill.developer=developer
            skill.save()
            return redirect("developers:developers_list")
        else:
            return render(request, self.template_name, {
                    'dev_form': dev_form,
                    'skill_form': skill_form
                })



def projectsList(request):
    projects=ProjectModel.objects.all()
    context={
        "projects":projects
    }
    return render(request,"developers/projectsList.html",context)

def projectsDetails(request,id):
    project=get_object_or_404(ProjectModel,id=id)
    context={
        "project":project
    }
    return render(request,"developers/projectsDetails.html",context)

def projectCreate(request):
    if request.method == "POST":
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            project = ProjectModel.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"]
            )
            project.developers.set(form.cleaned_data["developers"])

            return redirect("developers:projects_detail", id=project.id)
    else:
        form = forms.ProjectForm()

    return render(request, "forms/project_creat_form.html", {"form": form})

