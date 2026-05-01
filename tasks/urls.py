from django.urls import path
from .views import TaskListCreateView, TaskDetailView, DashboardView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]

# Dashboard URL will be registered in main urls.py or here:
dashboard_urls = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
