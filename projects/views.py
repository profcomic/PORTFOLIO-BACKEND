from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from django.http import JsonResponse
from .utils import get_github_stats
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

def github_status_view(request):
    # Replace 'yourusername' with your actual GitHub handle
    stats = get_github_stats('yourusername') 
    return JsonResponse(stats)


@api_view(['POST'])
def contact_view(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    if name and email and message:
        # LOGIC: Here is where you would send an email or save to DB
        print(f"New Message from {name} ({email}): {message}")
        return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)
    
    return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def home_view(request):
    return Response({
        "message": "Welcome to the Portfolio API",
        "endpoints": {
            "projects": "/api/projects/",
            "github_status": "/api/github-status/",
            "contact": "/api/contact/",
            "admin": "/admin/"
        }
    })


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('custom_admin:dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'projects/login.html', {'form': form})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('custom_login')
    
    # Get projects data for dashboard
    projects = Project.objects.all().order_by('-created_at')
    
    context = {
        'projects': projects[:5],  # Show latest 5 projects
        'total_projects': projects.count(),
        'user': request.user,
    }
    return render(request, 'admin/dashboard.html', context)


def custom_logout_view(request):
    logout(request)
    return redirect('custom_login')