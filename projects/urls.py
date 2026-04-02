from django.urls import path
from django.contrib import admin
from .views import ProjectList, github_status_view, contact_view, custom_login_view, dashboard_view

urlpatterns = [
    path('', custom_login_view, name='custom_login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('api/projects/', ProjectList.as_view(), name='project-list'),
    path('api/github-status/', github_status_view, name='github-status'),
    path('api/contact/', contact_view, name='contact'),
]