from re import template
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UpdateUserForm

from django.views.generic.edit import UpdateView

User = get_user_model()

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')
  
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'profile.html'
    success_message = "Successfully Updated"
    fields = [
        "email",
        "first_name",
        "last_name",
    ]
    success_url ="/"