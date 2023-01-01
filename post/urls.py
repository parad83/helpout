from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from ia import settings

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts/<category>/', views.posts, name='posts'),
    path('create/', views.create_post, name='create-post-view'),
    path('p/<id>/', views.post_details, name='post-details'),
    path('p/edit/<id>/', views.edit_post, name='edit-post'),
    path('p/delete/<id>/', views.delete_post, name='delete-post'),
    
    path('', views.home_view, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
