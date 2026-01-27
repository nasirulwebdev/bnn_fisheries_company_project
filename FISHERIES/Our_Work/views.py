from django.shortcuts import render
from .models import OurWork


def our_work_list_view(request):
    works = OurWork.objects.filter(is_active=True)

    context = {
        'works': works
    }
    return render(request, 'Our_Work/our_work.html', context)
