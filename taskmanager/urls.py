from django.contrib import admin
from django.urls import path, include
from tasks.views import DashboardView
from taskmanager.views import login_view, signup_view, dashboard_view, projects_view, tasks_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/dashboard/', DashboardView.as_view(), name='api-dashboard'),
    
    path('', dashboard_view, name='dashboard-ui'),
    path('login/', login_view, name='login-ui'),
    path('signup/', signup_view, name='signup-ui'),
    path('projects/', projects_view, name='projects-ui'),
    path('tasks/', tasks_view, name='tasks-ui'),
]
