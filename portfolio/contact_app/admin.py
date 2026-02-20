from django.contrib import admin

# Register your models here.
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'email', 'timestamp')
    
    
    search_fields = ('name', 'email')
    list_filter = ('timestamp',)
    
    readonly_fields = ('name', 'email', 'message', 'timestamp')