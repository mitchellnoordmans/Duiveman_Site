
from django.contrib import admin
from django.urls import path
from core.views import ( home, diensten,
                         offerte, spuitwerk, stucwerk, 
                         sierpleister, sauzen, lijstwerk, contact,
                          disclaimer, privacy, afbouw, muurschildering, overige_diensten )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('offerte/', offerte, name='offerte'),
    path('diensten/', diensten, name='diensten'),
    path('spuitwerk/', spuitwerk, name='spuitwerk'),
    path('stucwerk/', stucwerk, name='stucwerk'),
    path('sierpleister/', sierpleister, name='sierpleister'),
    path('sauzen/', sauzen, name='sauzen'),
    path('lijstwerk/', lijstwerk, name='lijstwerk'),
    path('contact/', contact, name='contact'),
    path('disclaimer/', disclaimer, name='disclaimer'),
    path('privacy/', privacy, name='privacy'),
    path('afbouw/', afbouw, name='afbouw'),
    path('muurschildering', muurschildering, name='muurschildering'),
    path('overige_diensten/', overige_diensten, name='overige_diensten'),
]

