from django.shortcuts import render
from .models import Publication


def publication_list_view(request):
    publications = Publication.objects.filter(is_active=True)

    context = {
        'publications': publications
    }
    return render(request, 'Publications/publications.html', context)
