
from django.contrib import admin
from django.urls import path
from core.views import home, diensten, offerte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('offerte/', offerte, name='offerte'),
    path('diensten/', diensten, name='diensten'),
    
]
