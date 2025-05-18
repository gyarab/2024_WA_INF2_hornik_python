# content/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Band, Genre

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

    # Hledání a řazení
    search_query = request.GET.get('search')
    sort_option = request.GET.get('sort')

    if search_query:
        albums = albums.filter(title__icontains=search_query)

    if sort_option == 'title_asc':
        albums = albums.order_by('title')
    elif sort_option == 'title_desc':
        albums = albums.order_by('-title')
    elif sort_option == 'year_asc':
        albums = albums.order_by('release_date')
    elif sort_option == 'year_desc':
        albums = albums.order_by('-release_date')

    return render(request, 'content/band_detail.html', {
        'band': band,
        'albums': albums,
        'search_query': search_query or '',
        'sort_option': sort_option or '',
    })

