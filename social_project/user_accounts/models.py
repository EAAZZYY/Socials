from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/%y/%m/%d",default="default.jpg")
    last_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    hobbies = models.CharField(max_length=300, blank=True)
    about_you = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.user.username