from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_date', 'created_at', 'get_tech_stack_display')
    list_filter = ('project_date', 'created_at', 'tech_stack')
    search_fields = ('title', 'description', 'tech_stack')
    readonly_fields = ()
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'project_date')
        }),
        ('Technical Details', {
            'fields': ('tech_stack', 'github_url', 'live_demo')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    
    def get_tech_stack_display(self, obj):
        return obj.get_tech_stack_display()
    get_tech_stack_display.short_description = 'Technologies'

