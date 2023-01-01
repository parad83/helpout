from django.contrib import admin
from . import models

@admin.register(models.Organisation)
class AdminOrganisation(admin.ModelAdmin):
    list_display = [
        'user',
        'name',
        'image',
        'verified'
    ]
    search_fields = [
        'user',
        'name',
    ]
    prepopulated_fields = {
        'slug': ['name']
    }
    list_filter = (
        'verified', 
        'date_joined', 
    )