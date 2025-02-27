from django.shortcuts import render
import json

def homepage(request):
    with open('bands.json', encoding='utf-8') as f:
        bands = json.load(f)

    return render(request, 'templates/content/homepage.html')
    