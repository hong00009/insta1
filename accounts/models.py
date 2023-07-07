from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from posts.models import Post
# Create your models here.


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')

    # profile_image = models.ImageField(upload_to='profiles')

    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle','center'],
        upload_to='profiles',
        )
    bookmarks = models.ManyToManyField(  #user와 Post연결, 'Bookmark'를 통해 연결,
        Post,
        through='Bookmark',
        related_name='bookmark_users',
    )

    
class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    