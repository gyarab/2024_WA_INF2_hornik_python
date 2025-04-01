from django.shortcuts import render, get_object_or_404
from .models import Band, Album, Track

def homepage(request):
    return render(request, "content/homepage.html")

def band_list(request):
    bands = Band.objects.all()
    return render(request, "content/band_list.html", 
                  {"bands": bands
                   })

def album_list(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    albums = Album.objects.filter(band=band)
    return render(request, "content/album_list.html", 
                  {"band": band, 
                   "albums": albums
                   })

def track_list(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album=album)
    return render(request, "content/track_list.html", 
                  {"album": album, 
                   "tracks": tracks
                   })
