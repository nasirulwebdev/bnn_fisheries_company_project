from django.shortcuts import render
from .models import Event


def event_list_view(request):
    events = Event.objects.filter(is_active=True)

    context = {
        'events': events
    }
    return render(request, 'Events/events.html', context)
