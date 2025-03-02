from django.contrib import admin
from django.urls import path
from content.views import homepage, hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('hello', hello),
]
