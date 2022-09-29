from django.shortcuts import render
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.conf import settings
from requests import delete

from .forms import *

def newsletter_signup(request):
    form = NewsletterUserForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Email already exists.')
        else:
            instance.save()
            messages.success(request, 'Hemos enviado un correo electrónico a tu dirección para que puedes continuar.')
            # Envío de correo
            subject = 'Libro de Python'
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            template = 'newsletters/email_templates/welcome.html'
            msg = render_to_string(template)
            send_msg = EmailMessage(subject, msg, from_email, to_email)
            send_msg.content_subtype= 'html'
            send_msg.send()

    context = {'form': form}
    return render(request, 'newsletters/start.html', context)


def newsletter_unsuscribe(request):
    form = NewsletterUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        user = NewsLetterUser.objects.filter(email=instance.email).exists()
        if user:
            user.delete()
            messages.success(request, 'Tu suscripción ha sido eliminada.')
        else:
           messages.warning(request, 'Email no encontrado.') 

    context = {'form': form}
    return render(request, 'newsletters/unsuscribe.html', context)