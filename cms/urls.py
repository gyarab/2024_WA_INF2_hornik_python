# urls.py
from django.urls import path
from content import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.homepage, name='homepage'),
    path('band/<int:band_id>/', views.band_detail, name='band_detail'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
]
