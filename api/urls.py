from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from ia import settings

urlpatterns = [
    # path('places/', views.places_api, name='places_api'),
    path('test/', views.test_api, name='test-api'),
    path('city/', views.cities_api, name='cities-api'),
    path('voiv/', views.voiv_api, name='voiv-api'),
    path('cat/', views.categories_api, name='cat-api'),
]
