#blog/views.py

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def title(request):
    return render(request, 'blog/title.html')

