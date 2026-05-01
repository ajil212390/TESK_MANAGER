from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsProjectMemberForTask
from rest_framework.views import APIView
from django.utils import timezone
from datetime import date
from django.db.models import Q

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        from django.db.models import Q
        if user.role == 'admin':
            return Task.objects.filter(Q(project__created_by=user) | Q(project__members=user)).distinct()
        return Task.objects.filter(assigned_to=user)

    def create(self, request, *args, **kwargs):
        if request.user.role != 'admin':
            return Response({"detail": "Only admins can create tasks."}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMemberForTask]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Task.objects.all()
        return Task.objects.filter(project__members=user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        if request.user.role != 'admin':
            # Members can only update status
            allowed_keys = ['status']
            data = {key: value for key, value in request.data.items() if key in allowed_keys}
        else:
            data = request.data

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == 'admin':
            tasks = Task.objects.filter(Q(project__created_by=user) | Q(project__members=user)).distinct()
        else:
            tasks = Task.objects.filter(assigned_to=user)

        today = timezone.now().date()
        
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(status='done').count()
        pending_tasks = tasks.exclude(status='done').count()
        overdue_tasks = tasks.filter(due_date__lt=today).exclude(status='done').count()

        data = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "overdue_tasks": overdue_tasks
        }
        return Response(data)
