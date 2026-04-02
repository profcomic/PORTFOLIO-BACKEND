from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.JSONField(default=list, help_text="List of technologies used")
    github_url = models.URLField(max_length=500, blank=True, null=True)
    live_demo = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_date = models.DateField(help_text="Date when the project was completed")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-project_date', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_stack_display(self):
        return ', '.join(self.tech_stack) if self.tech_stack else 'No technologies listed'

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)