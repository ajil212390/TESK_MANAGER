from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAdminOrReadOnly

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        from django.db.models import Q
        if user.role == 'admin':
            return Project.objects.filter(Q(created_by=user) | Q(members=user)).distinct()
        return Project.objects.filter(members=user).distinct()

    def perform_create(self, serializer):
        project = serializer.save(created_by=self.request.user)
        
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Project.objects.all()
        return Project.objects.filter(members=user).distinct()
