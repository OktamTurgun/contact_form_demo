from django.contrib import admin

# Register your models here.
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone", "email", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "message")
    list_filter = ('created_at',)
