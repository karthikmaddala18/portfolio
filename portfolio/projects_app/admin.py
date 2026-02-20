from django.contrib import admin

# Register your models here.
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'created_date', 'tech_stack')
    

    prepopulated_fields = {'slug': ('title',)}

    search_fields = ('title', 'tech_stack')
    list_filter = ('created_date', 'tech_stack')
    

    ordering = ('-created_date',)

from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date_earned')