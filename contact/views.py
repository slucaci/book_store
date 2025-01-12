from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
     
        if not name or not email or not message:
            messages.error(request, "All fields are required.")
            return render(request, "contact.html")
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Thank you for your message! We'll get back to you shortly.")
        return render(request, "contact.html", {})
    return render(request, "contact.html")
