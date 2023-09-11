from django.shortcuts import render, redirect
from .forms import OfferteForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def offerte(request):
    if request.method == 'POST':
        form = OfferteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a thank you page or some other appropriate action
            return redirect('bedankt')
    else:
        form = OfferteForm()
    
    return render(request, 'offerte.html', {'form': form})


def diensten(request):
    return render(request, 'diensten.html')

def spuitwerk(request):
    return render(request, 'spuitwerk.html')

def stucwerk(request):
    return render(request, 'stucwerk.html')

def sierpleister(request):
    return render(request, 'sierpleister.html')

def sauzen(request):
    return render(request, 'sauzen.html')

def lijstwerk(request):
    return render(request, 'lijstwerk.html')

def contact(request):
    return render(request, 'contact.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')

def privacy(request):
    return render(request, 'privacy.html')

def afbouw(request):
    return render(request, 'afbouw.html')

def muurschildering(request):
    return render(request, 'muurschildering.html')

def overige_diensten(request):
    return render(request, 'overige_diensten.html')