from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from .models import *
from django.views.generic import *
from . import forms
from django.urls import reverse_lazy



class DevelopersList(LoginRequiredMixin,ListView):
    model=DevelopersModel
    template_name = "developers/developersList.html"


class DeveloperDetails(LoginRequiredMixin,DetailView):
    model=DevelopersModel
    slug_url_kwarg="username"
    template_name = "developers/developersDetails.html"
    slug_field="username"

class DeveloperCreativeView(LoginRequiredMixin,CreateView):
    model=DevelopersModel
    template_name="forms/developers_create_form.html"
    form_class= forms.DevelopersForms

    def get(self, request):
        dev_form = forms.DevelopersForms()
        skill_form = forms.SkillForm()
        return render(request, self.template_name, {
            'dev_form': dev_form,
            'skill_form': skill_form
        })
        
    def form_valid(self,dev_form,skill_form):
        developer=dev_form.save()
        skill=skill_form.save(commit=False)
        skill.developer=developer
        skill.save()
        return redirect("developers:developers_list") 
    
    def form_invalid(self,request,dev_form,skill_form):
        return render(request, self.template_name, {
                    'dev_form': dev_form,
                    'skill_form': skill_form
                })
       
    def post(self, request, *args, **kwargs):
        dev_form=forms.DevelopersForms(request.POST)
        skill_form=forms.SkillForm(request.POST)
        if dev_form.is_valid() and skill_form.is_valid():
            return self.form_valid(dev_form , skill_form)
        else:
            return self.form_invalid(request,dev_form,skill_form)
                
        

class DeveloperUpdateView(LoginRequiredMixin,UpdateView):
    model=DevelopersModel
    template_name="forms/developersUpdate.html"
    fields=["first_name","last_name","email","username","age","projects"]
    slug_field="username"
    slug_url_kwarg="username"
    # add skill form for add new skill to developers


class DeveloperDeleteView(LoginRequiredMixin,DeleteView):
    model = DevelopersModel
    template_name = "forms/developerDelete.html"
    success_url = reverse_lazy("developers:developers_list")  # مسیر بازگشت بعد از حذف
    slug_field = "username"       # اگر حذف بر اساس username است
    slug_url_kwarg = "username"

class ProjectListView(LoginRequiredMixin,ListView):
    model=ProjectModel
    template_name="developers/projectsList.html"

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model =ProjectModel
    pk_url_kwarg="id"
    template_name="developers/projectsDetails.html"



class ProjectCreateView(LoginRequiredMixin,CreateView):
    model=ProjectModel
    template_name="forms/project_creat_form.html"
    form_class=forms.ProjectForm

    def form_valid(self,form):
        proj =form.save()
        developers=form.cleaned_data["developers"]
        proj.developers.set(developers)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class ProjectUpdataView(LoginRequiredMixin,UpdateView):
    model=ProjectModel
    form_class=forms.ProjectForm
    template_name="forms/projectUpdata.html"
    pk_url_kwarg="id"
    
    def form_valid(self, form):
        project = form.save()
        developers = form.cleaned_data.get("developers")
        project.developers.set(developers)
        return super().form_valid(form)
    
class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = ProjectModel
    template_name = "forms/projectDelete.html"
    success_url = reverse_lazy("developers:projects_list")  
    pk_url_kwarg = "id"


# error handeling and H-case
#form validation
#   clean
#clean code
#django massege


