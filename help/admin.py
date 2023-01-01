from django.contrib import admin
from . import models

@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'title',
        'date'
    ]
    search_fields = [
        'email',
        'title',
    ]
    list_filter = (
        'date',
    )
