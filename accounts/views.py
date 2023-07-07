from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if  form.is_valid():
            user = form.save()
            auth_login(request, user)
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
    # user_info = User.objects.get(username=username)
    user_info = get_object_or_404(User, username=username)

    context = {
        'user_info' : user_info,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def following(request, id):
    User = get_user_model()

    me = request.user # 팔로우 버튼 클릭한 사람
    you = User.objects.get(id=id) # 팔로우 하려는 사람

    if me != you:
        # if me in you.follower.all() 기준점이 달라도 실행은 같음
        if you in me.following.all():
            me.following.remove(you)
        else:
            me.following.add(you)

    return redirect('accounts:profile', you.username)

@login_required
def edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/form.html', context)

@login_required
def bookmark_list(request):
    bookmarks = request.user.bookmark_set.all().order_by('-created_at') #유저가 가진 북마크 목록

    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'accounts/bookmark_list.html', context)


def newsfeed(request):

    user = request.user
    posts = Post.objects.filter(user__in=user.following.all())
    
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)