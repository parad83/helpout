"""
Django settings for ia project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!=kmm41wx+0y)abx#a99cyf-ypokn0ztn60$s^%$b3&-y!*6&&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '10.48.53.245',
    '127.0.0.1',
    '0.0.0.0',
    '192.168.1.81',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    'account',
    'post',
    'report',
    'organisation',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'ia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ia.wsgi.application'

AUTHENTICATION_BACKENDS = ['account.backends.EmailBackend']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ia-cs',
        'USER': 'root',
        'PASSWORD': 'niewiemjakiehaslo',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = os.path.join(BASE_DIR, '/static/')
STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, '/static/')
# ]

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media/')

# MEDIA_URL = '/images/'
MEDIA_URL = os.path.join(BASE_DIR, '/media/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://maps.googleapis.com',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'for.test.purposes.1337@gmail.com'
EMAIL_HOST_PASSWORD = 'jagquc-5piddi-wArcek'


EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'django.test1@outlook.com'
EMAIL_HOST_PASSWORD = '@):KBA-fi)o)gZXuB'

LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MESSAGE_TAGS = {
    messages.DEBUG: 'msg-info',
    messages.INFO: 'msg-info',
    messages.SUCCESS: 'msg-success',
    messages.WARNING: 'msg-warning',
    messages.ERROR: 'msg-danger',
}