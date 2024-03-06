from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Posts(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user')
    title = models.CharField(max_length=50, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to="media/%d/%m/%y",blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like",blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length = 250)
    posted_on = models.DateTimeField(auto_now_add=True)
    comment_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.comment