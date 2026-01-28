from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event


def event_list_view(request):
    query = request.GET.get('q', '')
    events = Event.objects.filter(is_active=True)
    
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'events': events
    }
    return render(request, 'Events/events.html', context)
