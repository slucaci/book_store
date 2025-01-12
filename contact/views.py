from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Thank you for your message! We'll get back to you shortly.")

    return render(request, "contact.html")
