from django.shortcuts import render
from .models import AboutPage


def about_view(request):
    about = AboutPage.objects.filter(is_active=True).first()

    context = {
        'about': about
    }
    return render(request, 'About/about.html', context)
