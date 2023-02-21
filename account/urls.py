from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('join/', views.signup_view, name='join'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('u/<user_id>/', views.account_view, name='account-view'),
    path('edit/', views.edit_account, name='edit-account'),
    path('delete/', views.delete_account, name='delete-account'),
    
    path('reset/', views.reset_generate_link, name='generate-email'),
    path('reset/sent/', views.reset_email_sent, name='email-sent'),
    path(r'reset/<uidb64>/<token>/', views.reset_password, name='reset-password'),
    
    path('thankyou/', views.join_message, name='join-message'),
    path('tos/', views.tos, name='tos'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
]