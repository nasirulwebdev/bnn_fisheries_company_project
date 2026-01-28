from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Publication


def publication_list_view(request):
    publications = Publication.objects.filter(is_active=True)
    query = request.GET.get('q', '')
    
    if query:
        publications = publications.filter(title__icontains=query)
    
    paginator = Paginator(publications, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'publications': publications
    }
    return render(request, 'Publications/publications.html', context)
