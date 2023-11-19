from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class UserListView(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'home'

class Logout(LogoutView):
    next_page = 'home'
