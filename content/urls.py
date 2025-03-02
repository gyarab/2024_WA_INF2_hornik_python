from django.urls import path
from .views import homepage, BandListCreate, AlbumListCreate, BandDetail, AlbumDetail

urlpatterns = [
    path("", homepage, name="homepage"),
    path("bands/", BandListCreate.as_view(), name="band-list"),
    path("bands/<int:pk>/", BandDetail.as_view(), name="band-detail"),
    path("albums/", AlbumListCreate.as_view(), name="album-list"),
    path("albums/<int:pk>/", AlbumDetail.as_view(), name="album-detail"),
]
