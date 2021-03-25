from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm


def contact(request):
    contact_form = ContactForm

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            emial = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Envaimos el Emial
            email = EmailMessage(
                'La Caffetiera: Curso, Proyecyo Intermedio',
                'De {} <{}>\n\nEscribio:\n\n{}'.format(name, emial, content),
                'no-contestar@inbox.mailtrap.io',
                ['davidsanchezmotran@gmail.com'],
                reply_to=[emial]
            )

            try:
                # Si sale bien
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                # si Falla
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})
