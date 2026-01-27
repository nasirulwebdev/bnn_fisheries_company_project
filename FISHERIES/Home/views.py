from django.shortcuts import render
from .models import Banner, Feature

def home_view(request):
    banners = Banner.objects.all()
    features = Feature.objects.all()
    context = {
        'banners': banners,
        'features': features
    }
    return render(request, 'Home/home.html', context)
