from django.db import models
from ia import settings

class Organisation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='organisations')
    biography = models.CharField(max_length=255)
    website = models.URLField()
    verified = models.BooleanField(default=False)
    slug = models.SlugField()
    date_joined = models.DateTimeField(auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['verified']

