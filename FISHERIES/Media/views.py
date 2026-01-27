from django.shortcuts import render
from .models import Media


def media_list_view(request):
    media_list = Media.objects.filter(is_active=True)

    context = {
        'media_list': media_list
    }
    return render(request, 'Media/media.html', context)
