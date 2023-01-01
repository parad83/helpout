from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.shortcuts import redirect
from ia import settings
import shortuuid
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseForbidden
from datetime import datetime, timezone

WORDLIST = '/Users/parad/IES/CS/IA/bad-words.txt'

def validate_first_name(name):
    if len(name.split()) != 1:
        raise ValidationError("Name should't contain any spaces")
    else:
        return name
    
def profanity_filter(string):
    if len(string) > 3:
        with open(WORDLIST, 'r') as f:
            for line in f:
                if string in line:
                    raise ValidationError("Don't use any inappropriate words 🤬")
    return string
            
def email_profanity_filter(email):
    string = email.split('@')[0]
    with open(WORDLIST, 'r') as f:
        for line in f:
            if string in line:
                raise ValidationError("Don't use any inappropriate words 🤬")
    return email

def length_check(string):
    if len(string) <= 3:
        raise ValidationError("Name should be at least 3 letters long")
    return string

def tos_check(value):
    if not value:
        raise ValidationError("Oops, You forgot about something 😜")
    return value

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('Email is required')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
        )
        user.set_password(password),
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    last_name = None
    id = models.CharField(max_length=10, editable=True, default=shortuuid.ShortUUID(alphabet="0123456789").random(length=10), primary_key=True, unique=True)
    email = models.EmailField(('email'), unique=True, validators=[email_profanity_filter])
    first_name = models.CharField(('name'), max_length=15, validators=[length_check, profanity_filter, validate_first_name])
    isd_code = models.CharField(max_length=4, default="+48", null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    has_organisation = models.BooleanField(default=False)
    rating = models.SmallIntegerField(default=10)
    can_have_organisation = models.BooleanField(default=False)
    can_create_posts = models.BooleanField(default=True)
    can_send_messages = models.BooleanField(default=True)
    can_report = models.BooleanField(default=True)
    accepts_tos = models.BooleanField(default=False, validators=[tos_check])
    display_phone = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['email']