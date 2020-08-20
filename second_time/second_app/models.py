from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=264)
    profile_pic = models.ImageField(upload_to = 'profile_pic', blank =True)

    def __str__(self):
        return self.user.username

class School(models.Model):
    name = models.CharField(max_length = 264)
    principal = models.CharField(max_length = 264)
    location = models.CharField(max_length = 264)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("second_app:school_detail_view", kwargs={"pk": self.pk})
    
class Student(models.Model):
    name = models.CharField(max_length = 264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("second_app:school_list_view")
    