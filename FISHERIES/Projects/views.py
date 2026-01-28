from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project

def project_list_view(request):
    projects = Project.objects.filter(is_active=True)
    query = request.GET.get('q', '')
    if query:
        projects = projects.filter(title__icontains=query)
    
    paginator = Paginator(projects, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'projects': projects
        }
    # image + video support template
    return render(request, 'Projects/projects_images_video.html', context)
