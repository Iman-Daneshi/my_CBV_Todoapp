from django.shortcuts import render
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'registration/register.html'
  success_url = reverse_lazy('accounts:login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
