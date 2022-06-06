from .models import *
from django.shortcuts import render
from django.contrib.auth.views import LoginView   
from django.contrib.auth import logout

    
class LoginView(LoginView):
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return  render(request, 'logout.html')