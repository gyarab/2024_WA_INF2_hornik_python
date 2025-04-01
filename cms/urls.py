from django.urls import path
from content import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Hlavní stránka s kapelami
    path('band/<int:band_id>/', views.band_detail, name='band_detail'),  # Detail kapely
]
