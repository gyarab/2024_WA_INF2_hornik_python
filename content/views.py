import json
from django.shortcuts import render
from django.conf import settings
import os

def homepage(request):
    # Cesta k souboru s daty
    json_file_path = os.path.join(settings.BASE_DIR, 'content', 'fixtures', 'bands.json')
    
    # Načteme data z JSON souboru
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Předáme data do šablony
    return render(request, 'content/homepage.html', {'bands': data})

def band_detail(request, band_id):
    # Cesta k souboru s daty
    json_file_path = os.path.join(settings.BASE_DIR, 'static', 'content', 'data', 'bands.json')
    
    # Načteme data z JSON souboru
    with open(json_file_path, 'r', encoding='utf-8') as f:
        bands = json.load(f)
    
    # Najdeme kapelu podle ID
    band = next((band for band in bands if band['id'] == band_id), None)

    # Pokud kapela neexistuje, vrátíme 404
    if band is None:
        return render(request, 'content/404.html')
    
    # Předáme data do šablony
    return render(request, 'content/band_detail.html', {'band': band})
