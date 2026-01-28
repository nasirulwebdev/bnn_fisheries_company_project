from django.shortcuts import render
from .models import Project

def project_list_view(request):
    projects = Project.objects.filter(is_active=True)
    context = {'projects': projects}
    # image + video support template
    return render(request, 'Projects/projects_images_video.html', context)
