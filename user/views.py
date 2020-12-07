from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'successfully signup !!')
    else:
        fm = SignupForm()
    return render(request, 'signup.html', {'form': fm})


def login_user(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully')
                return redirect("home")

    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def dashboard(request):
    return render(request, 'dashboard.html')


def logout_user(request):
    logout(request)
    return redirect("login")
