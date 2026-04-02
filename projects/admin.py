from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # This makes the admin list look clean and professional
    list_display = ('title', 'created_at')
    search_fields = ('title', 'tech_stack')
