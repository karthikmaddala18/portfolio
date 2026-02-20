from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_body = request.POST.get('message')

       
        ContactMessage.objects.create(name=name, email=email, message=message_body)

        send_mail(
            subject=f"New Portfolio Message from {name}",
            message=f"You received a message: \n\n{message_body}\n\nFrom: {email}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        send_mail(
            subject="Message Received - Thank You!",
            message=f"Hi {name}, thank you for reaching out. I have received your message and will get back to you soon.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Your message was sent and confirmed via email!")
        return redirect('contact')

    return render(request, 'contact.html')