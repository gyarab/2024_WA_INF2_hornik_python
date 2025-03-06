from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

def homepage(request):
    with open('bands.json', encoding='utf-8') as f:
        bands = json.load(f)

    return render(request, 'content/homepage.html', {'bands': bands})

def article(request, id):
    with open('bands.json', encoding='utf-8') as f:
        bands = json.load(f)

    article = bands[id]
    return render(request, 'content/bands.html', {'article': article})