from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=264)
    profile_pic = models.ImageField(upload_to = 'profile_pic', blank =True)

    def __str__(self):
        return self.user.username