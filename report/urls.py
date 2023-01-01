from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('p/<post_id>/', views.report_post, name='report-post'),
]
