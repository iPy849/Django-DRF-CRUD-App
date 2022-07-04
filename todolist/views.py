from .models import Task
from .serializers import TaskSerializer, TaskDetailSerializer
from rest_framework import generics
from rest_framework import permissions



class SnippetList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer