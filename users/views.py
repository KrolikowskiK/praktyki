from django.contrib.auth import login, authenticate
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm

def user_signup(request):
    """
    Manages user sign up with CustomUserCreationForm.
    If credentials are valid, redirects user to temporary 'logged in' page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return HttpResponse("You're logged in")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_signup.html', {'form': form})

class UserLoginView(LoginView):
    """
    Manages user sign in with CustomUserAuthenticationForm 
    which is passed as an argument to as_view function in mysite/urls.py.
    Redirects user to /logged/ temporary url.
    """
    template_name = 'users/user_signin.html'
    extra_context = {
        'next': '/logged/',
    }

def logged_in(request):
    return HttpResponse("You're logged in")
