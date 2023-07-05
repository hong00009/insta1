from django.db import models
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
# Create your models here.

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='pic/%m/%d')
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle','center'],
        upload_to='pic/%m/%d',
    )

    like_users = models.ManyToManyField(get_user_model(), related_name='like_posts')
    # 유저와 연결, 접근할때의 이름은 like_posts로 설정하여
    # post.like_user.all() 또는 user.like_posts.all()로 접근

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)