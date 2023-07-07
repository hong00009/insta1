from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    posts = Post.objects.all()
    comment_form = CommentForm()

    context = {
        'posts' : posts,
        'comment_form' : comment_form,
    }

    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')

    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/form.html', context)

@login_required
def delete(request, id):
    post = Post.objects.get(id=id)
    
    post.delete()
    
    return redirect('posts:index') 

@login_required
def comments_create(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('posts:index')
        
@login_required        
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)
    
    # user.like_posts.add(post)
    # post.like_user.add(user) 도 가능
    
    # ex) 게시물을 좋아요누른사람중 3번유저가 존재한다면
    # 이미 좋아요 누름
    # if post.like_users.filter(id=user.id).exists():

    # 유저가 들어있는지, 좋아요를 누른 전체목록에서
    if user in post.like_users.all():
        user.like_posts.remove(post)

    #아직 좋아요 안누름
    else:
        user.like_posts.add(post)


    return redirect('posts:index')

@login_required
def bookmarks(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    # if user in post.bookmark_users.all():  유저기준
    if post in user.bookmarks.all(): #게시물기준
        user.bookmarks.remove(post)
    else:
        user.bookmarks.add(post)

    return redirect('posts:index')