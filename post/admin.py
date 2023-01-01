from django.contrib import admin
from . import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'title',
        'date_created',
        'rating',
        'visible'
    ]
    search_fields = [
        'author',
        'title',
        'text',
        'date_created',
        'rating'
    ]
    list_filter = (
        'rating',
        'visible',
        'date_created',
        'date_updated',
    )
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'icon',
        'id'
    ]
    search_fields = [
        'name',
    ]