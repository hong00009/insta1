from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form
    }

    return render(request, 'accounts/form.html', context)
# accounts/form은 회원가입할때, 로그인할때 사용

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

        
    else:
        form = CustomAuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def profile(request, username):
    User = get_user_model()
    user_info = User.objects.get(username=username)
    
    context = {
        'user_info' : user_info,
    }
    return render(request, 'accounts/profile.html', context)