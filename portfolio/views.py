import pdfkit # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Portfo
from .forms import PortfoForm
from django.template.loader import render_to_string # type: ignore

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
