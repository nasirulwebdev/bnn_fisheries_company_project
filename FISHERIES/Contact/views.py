from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        if name and email and subject and message_text:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )
            messages.success(request, "আপনার বার্তা সফলভাবে পাঠানো হয়েছে।")
            return redirect('contact')
        else:
            messages.error(request, "অনুগ্রহ করে সব তথ্য পূরণ করুন।")

    return render(request, 'Contact/contact.html')
