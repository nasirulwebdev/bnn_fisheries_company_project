from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Media


def media_list_view(request):
    query = request.GET.get('q', '')
    media_list = Media.objects.filter(is_active=True)
    
    paginator = Paginator(media_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'media_list': media_list
    }
    return render(request, 'Media/media.html', context)
