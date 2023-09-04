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



