from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from django.http import JsonResponse
from .utils import get_github_stats
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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