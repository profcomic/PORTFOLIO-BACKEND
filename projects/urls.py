from django.urls import path
from .views import ProjectList, github_status_view, contact_view

urlpatterns = [
    path('api/projects/', ProjectList.as_view(), name='project-list'),
    path('api/github-status/', github_status_view, name='github-status'),
    path('api/contact/', contact_view, name='contact'),
]