import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def load_bands():
    """Načte data z JSON souboru"""
    with open('content/fixtures/bands.json', 'r') as file:
        data = json.load(file)
    return data

def homepage(request):
    """Zobrazení seznamu kapel na hlavní stránce"""
    bands = load_bands()  # Načteme kapely z JSON souboru
    return render(request, 'content/homepage.html', {'bands': bands})

def band_detail(request, band_id):
    bands = load_bands()  # Načteme kapely z JSON souboru
    band = next((band for band in bands if band['id'] == band_id), None)
    
    if band is None:
        return HttpResponse("Kapela nenalezena.", status=404)
    
    return render(request, 'content/band_detail.html', {'band': band})
