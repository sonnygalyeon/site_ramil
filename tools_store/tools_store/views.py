from pyexpat.errors import messages

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Your account has been created!')
            return redirect('')  # Redirect to home page after registration
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'


@login_required
def logged_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, 'login.html')


def store(request):
    return render(request, "store.html")


def account_info(request):
    return render(request, "account_info.html")


def about_info(request):
    return render(request, "about_info.html")


def register_user(request):
    return render(request, "register_user.html")
