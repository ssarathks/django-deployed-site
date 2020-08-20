from django.contrib import admin
from second_app.models import UserProfileInfo,Student,School
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(School)
admin.site.register(Student)