# Create your views here.
from django.shortcuts import render, get_object_or_404  # type: ignore[reportMissingModuleSource]
from .models import Notice


# All Notice Page

def notice_list(request):
    notices = Notice.objects.filter(is_active=True)

    context = {
        'notices': notices
    }

    return render(request, 'Notice/notice_list.html', context)


# Notice Details Page

def notice_detail(request, id):
    notice = get_object_or_404(
        Notice,
        id=id,
        is_active=True
    )

    context = {
        'notice': notice
    }

    return render(request, 'Notice/notice_detail.html', context)
