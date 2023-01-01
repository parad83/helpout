from django.db import models
from ia import settings
import post

class ReportPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(post.models.Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        

class ReportUser(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reporting')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='being_reported')
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    
    class Meta:
        ordering = ['-date']