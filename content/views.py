# content/views.py
from django.shortcuts import render, get_object_or_404
from .models import Band

def homepage(request):
    bands = Band.objects.all()  # Načteme všechny kapely
    return render(request, 'content/homepage.html', {'bands': bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)  # Najdeme kapelu podle ID
    albums = band.album.all()  # Načteme všechna alba této kapely
    return render(request, 'content/band_detail.html', {'band': band, 'albums': albums})
