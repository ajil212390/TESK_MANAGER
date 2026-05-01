from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def projects_view(request):
    return render(request, 'projects.html')

def tasks_view(request):
    return render(request, 'tasks.html')
