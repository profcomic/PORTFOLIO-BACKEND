from django.urls import path
from projects.views import dashboard_view, custom_logout_view

app_name = 'custom_admin'

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('projects/', dashboard_view, name='project_list'),  # Temporary - pointing to dashboard
    path('projects/create/', dashboard_view, name='project_create'),  # Temporary - pointing to dashboard
    path('projects/<int:pk>/edit/', dashboard_view, name='project_edit'),  # Temporary - pointing to dashboard
    path('projects/<int:pk>/delete/', dashboard_view, name='project_delete'),  # Temporary - pointing to dashboard
    path('logout/', custom_logout_view, name='logout'),
    # Add more admin URLs here as needed
]
