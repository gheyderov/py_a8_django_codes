from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    photo = models.ImageField('photo', upload_to='user_profiles/', null=True, blank=True)
    bio = models.CharField('bio', max_length=255, null=True, blank=True)

    def get_image(self):
        if self.photo:
            return self.photo.url
        return '/static/images/nophoto.jpeg/'
    