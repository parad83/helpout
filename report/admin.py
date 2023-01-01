from django.contrib import admin
from . import models

@admin.register(models.ReportUser)
class ReportUserAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'user',
        'date'
    ]
    search_fields = [
        'author',
        'user',
    ]
    
@admin.register(models.ReportPost)
class ReportPostAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'post',
        'date'
    ]
    search_fields = [
        'user',
        'post',
    ]
