from django.urls import path
from content.views import homepage, band_list, album_list, track_list

urlpatterns = [
    path('', homepage, name="homepage"),
    path('bands/', band_list, name="band_list"),
    path('bands/<int:band_id>/albums/', album_list, name="album_list"),
    path('albums/<int:album_id>/tracks/', track_list, name="track_list"),
]
