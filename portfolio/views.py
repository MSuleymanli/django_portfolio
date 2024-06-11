from django.core.mail import EmailMessage # type: ignore
from django.contrib import messages # type: ignore
import pdfkit # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse,HttpResponseRedirect # type: ignore
from .models import Portfo,Contact
from .forms import PortfoForm,ContactForm
from django.template.loader import render_to_string # type: ignore
from django.conf import settings # type: ignore
from django.utils import translation # type: ignore
from django.urls.base import resolve, reverse # type: ignore
from django.urls.exceptions import Resolver404 # type: ignore
from urllib.parse import urlparse

import os
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltox\bin\wkhtmltopdf.exe') 
def home_view(request):
    form = PortfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("show")

    return render(request, 'home.html', {'form': form})

def show_view(request):
    portfolios = Portfo.objects.all()
    return render(request, 'show.html', {'portfolios': portfolios})

def download_pdf(request, pk):
    portfolio = get_object_or_404(Portfo, pk=pk)
    html = render_to_string('portfolio_pdf.html', {'portfolio': portfolio})
    pdf = pdfkit.from_string(html, False, configuration=PDFKIT_CONFIG)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="portfolio_{portfolio.pk}.pdf"'
    return response

def contact_show(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            html_message = render_to_string(
                "email.html",
                {
                    "name": contact.name,
                },
            )

            email_message = EmailMessage(
                subject="Yeni Müraciət",
                body=html_message,
                from_email="suleymanovmensur5@gmail.com",
                to=[contact.email],
            )

            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, "Müraciətiniz uğurla göndərildi...")
            return redirect("contact")
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {"form": form})

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response