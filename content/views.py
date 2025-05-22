from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Band, Genre

def homepage(request):
    genre_id = request.GET.get('genre')
    search_query = request.GET.get('search')
    sort_option = request.GET.get('sort')

    bands = Band.objects.all()

    if genre_id:
        bands = bands.filter(genre__id=genre_id)

    if search_query:
        bands = bands.filter(name__icontains=search_query)

    if sort_option == 'name':
        bands = bands.order_by('name')
    elif sort_option == 'genre':
        bands = bands.order_by('genre__name')
    elif sort_option == 'year':
        bands = bands.order_by('founded')

    genres = Genre.objects.all()
    latest_bands = Band.objects.order_by('-id')[:6]

    return render(request, 'content/homepage.html', {
        'bands': bands,
        'genres': genres,
        'selected_genre': int(genre_id) if genre_id else None,
        'latest_bands': latest_bands,
        'search_query': search_query or '',
        'sort_option': sort_option or '',
    })

def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    albums = band.album.all()

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
