from django.shortcuts import render, redirect # type: ignore
from .forms import PortfoForm
from .models import Portfo

def home_view(request):
    form = PortfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("show")
    
    return render(request, 'home.html', {'form': form})

def show_view(request):
    portfolios = Portfo.objects.all()
    return render(request, 'show.html', {'portfolios': portfolios})