from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name="auth"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='Authentication/password_change.html',success_url=reverse_lazy('auth:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='Authentication/password_change_done.html'), name='password_change_done'),
    path('signup/',SignUpView.as_view(),name="signup"),
]
