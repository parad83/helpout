from distutils.errors import PreprocessError
from uuid import UUID
from django.contrib import admin
from . import models
import shortuuid

UUID = shortuuid.ShortUUID(alphabet="0123456789").random(length=10)

@admin.register(models.User)
class AdminUser(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'phone_number',
        'rating'
    ]
    search_fields = [
        'email'
        'user',
        'phone_number'
    ]
    fieldsets = (
        (
            None, {
            'fields': (
                'email', 
                'first_name', 
                'isd_code', 
                'phone_number'
            )
            }
        ),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_staff', 'is_superuser', 'has_organisation', 'can_have_organisation', 'can_create_posts', 'can_send_messages', 'rating'),
        }),
    )
    list_filter = ( 
        'date_joined', 
        'rating',
    )