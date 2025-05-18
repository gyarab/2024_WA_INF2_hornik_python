# content/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Band, Genre, Album

def homepage(request):
    genre_id = request.GET.get('genre')
    search_query = request.GET.get('search')
    
    bands = Band.objects.all()

    if genre_id:
        bands = bands.filter(genre__id=genre_id)
    
    if search_query:
        bands = bands.filter(name__icontains=search_query)

    genres = Genre.objects.all()
    
    return render(request, 'content/homepage.html', {
        'bands': bands,
        'genres': genres,
        'selected_genre': int(genre_id) if genre_id else None
    })

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    albums = band.album.all()
    return render(request, 'content/band_detail.html', {'band': band, 'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    band = album.band
    return render(request, 'content/album_detail.html', {'album': album, 'band': band})
