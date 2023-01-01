from django.db import models
from account.models import profanity_filter

class Ticket(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=25, validators=[profanity_filter], blank=True, null=True)
    text = models.CharField(max_length=250, validators=[profanity_filter])
    date = models.DateTimeField(auto_created=True, auto_now_add=True)