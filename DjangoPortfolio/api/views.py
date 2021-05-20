from django.shortcuts import render, get_object_or_404
from .models import Project, Image, Tag, DetailBody

def home(request):
    return render(request, 'api/index.html')

def projects(request):
    projects = Project.objects
    return render(request, 'api/projects.html', {'projects':projects})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    images = Image.objects.filter(project_id=project_id)
    body = DetailBody.objects.filter(project_id=project_id)
    return render(request, 'api/detail.html', {'project':project_detail, 'images':images, 'body':body})

def contact(request):
    return render(request, 'api/contact.html')

