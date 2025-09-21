<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
=======
<<<<<<< HEAD

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> bb8d60eaff9c79db86becab91c8e18145f023ed4
>>>>>>> 7a1742b73cd26f85cb18ac9b75c565d609587f03
