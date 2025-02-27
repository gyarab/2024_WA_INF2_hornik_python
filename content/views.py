from django.shortcuts import render

def homepage(request):

    return render(request, 'content/homepage.html')
    