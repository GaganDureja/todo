from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer

class TasksListCreateAPIView(generics.ListCreateAPIView):
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer

class TasksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer
