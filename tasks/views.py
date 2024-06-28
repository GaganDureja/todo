from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer
from datetime import date

class TasksListCreateAPIView(generics.ListCreateAPIView):
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer

class TasksRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer

class DueTodayTaskListAPIView(generics.ListAPIView):
  serializer_class = TasksSerializer
  def get_queryset(self):
    return Tasks.objects.filter(due_date=date.today())
