from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    """Custom form for Project model with enhanced validation"""
    
    class Meta:
        model = Project
        fields = [
            'title', 'description', 'tech_stack', 
            'github_url', 'live_demo', 'image', 'project_date'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter project description'
            }),
            'tech_stack': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Django, React, PostgreSQL (comma-separated)'
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/username/repo'
            }),
            'live_demo': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'project_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
    
    def clean_tech_stack(self):
        """Clean and validate tech_stack field"""
        tech_stack = self.cleaned_data.get('tech_stack', '')
        if isinstance(tech_stack, str):
            # Convert comma-separated string to list
            tech_list = [tech.strip() for tech in tech_stack.split(',') if tech.strip()]
            return tech_list
        return tech_stack
    
    def clean_github_url(self):
        """Validate GitHub URL"""
        url = self.cleaned_data.get('github_url')
        if url and 'github.com' not in url.lower():
            raise forms.ValidationError('Please enter a valid GitHub URL')
        return url
    
    def clean(self):
        """Custom validation for the form"""
        cleaned_data = super().clean()
        github_url = cleaned_data.get('github_url')
        live_demo = cleaned_data.get('live_demo')
        
        # Ensure at least one URL is provided
        if not github_url and not live_demo:
            raise forms.ValidationError(
                'Please provide at least a GitHub URL or Live Demo URL'
            )
        
        return cleaned_data
