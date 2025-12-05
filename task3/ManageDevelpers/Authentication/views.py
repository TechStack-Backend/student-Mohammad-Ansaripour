from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUpView(CreateView):
    template_name = 'Authentication/signup.html'   
    form_class = UserCreationForm            
    success_url = reverse_lazy('auth:login')
    
class ProfileDetailView(LoginRequiredMixin,DetailView):
    pass
    
    
class ProfleUpdateView(LoginRequiredMixin,UpdateView):
    pass

class ProfileDeleteView(LoginRequiredMixin,DeleteView):
    pass
