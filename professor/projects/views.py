from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from .models import Project
from .forms import ProjectForm
import json

@login_required
def custom_admin_dashboard(request):
    """Custom admin dashboard"""
    total_projects = Project.objects.count()
    recent_projects = Project.objects.order_by('-created_at')[:5]
    
    context = {
        'total_projects': total_projects,
        'recent_projects': recent_projects,
        'page_title': 'Admin Dashboard'
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def project_list(request):
    """List all projects with search and pagination"""
    search_query = request.GET.get('search', '')
    page_number = request.GET.get('page', 1)
    
    projects = Project.objects.all()
    
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(tech_stack__icontains=search_query)
        )
    
    paginator = Paginator(projects, 10)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'page_title': 'Projects'
    }
    return render(request, 'admin/project_list.html', context)

@login_required
def project_create(request):
    """Create a new project"""
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, f'Project "{project.title}" created successfully!')
            return redirect('custom_admin:project_list')
    else:
        form = ProjectForm()
    
    context = {
        'form': form,
        'page_title': 'Create Project',
        'action': 'Create'
    }
    return render(request, 'admin/project_form.html', context)

@login_required
def project_edit(request, pk):
    """Edit an existing project"""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            messages.success(request, f'Project "{project.title}" updated successfully!')
            return redirect('custom_admin:project_list')
    else:
        form = ProjectForm(instance=project)
    
    context = {
        'form': form,
        'project': project,
        'page_title': 'Edit Project',
        'action': 'Edit'
    }
    return render(request, 'admin/project_form.html', context)

@login_required
def project_delete(request, pk):
    """Delete a project"""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        title = project.title
        project.delete()
        messages.success(request, f'Project "{title}" deleted successfully!')
        return redirect('custom_admin:project_list')
    
    context = {
        'project': project,
        'page_title': 'Delete Project'
    }
    return render(request, 'admin/project_delete.html', context)

@csrf_exempt
@require_POST
@login_required
def project_delete_ajax(request, pk):
    """Delete project via AJAX"""
    project = get_object_or_404(Project, pk=pk)
    title = project.title
    project.delete()
    
    return JsonResponse({
        'success': True,
        'message': f'Project "{title}" deleted successfully!'
    })

@login_required
def project_stats(request):
    """Get project statistics for dashboard"""
    total = Project.objects.count()
    recent = Project.objects.filter(
        created_at__gte=timezone.now() - timezone.timedelta(days=30)
    ).count()
    
    return JsonResponse({
        'total_projects': total,
        'recent_projects': recent
    })
