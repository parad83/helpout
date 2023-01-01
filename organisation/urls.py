from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('o/<slug:slug>/', views.organisation_details, name='organisation-details'),
    path('organisations/', views.organisations, name='organisations-view'),
    path('organisations/create', views.create_organisation, name='create-organisation'),
    path('organisations/edit', views.edit_organisation, name='edit-organisation'),
    # path('organisations/request', views.request_organisation, name='request-organisation'),
]