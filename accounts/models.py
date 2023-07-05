from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
# Create your models here.


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')

    # profile_image = models.ImageField(upload_to='profiles')

    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle','center'],
        upload_to='profiles',
        )