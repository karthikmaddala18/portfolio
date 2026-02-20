from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from projects_app.models import Project
from contact_app.models import ContactMessage
from .serializers import ProjectSerializer, ContactMessageSerializer


class ProjectListAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_date')
    serializer_class = ProjectSerializer
  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer