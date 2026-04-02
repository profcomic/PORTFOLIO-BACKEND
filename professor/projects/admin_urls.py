from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    # Dashboard
    path('admin/', views.custom_admin_dashboard, name='dashboard'),
    
    # Projects
    path('admin/projects/', views.project_list, name='project_list'),
    path('admin/projects/create/', views.project_create, name='project_create'),
    path('admin/projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('admin/projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # AJAX endpoints
    path('admin/projects/<int:pk>/delete-ajax/', views.project_delete_ajax, name='project_delete_ajax'),
    path('admin/stats/', views.project_stats, name='project_stats'),
]
