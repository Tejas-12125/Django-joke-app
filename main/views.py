import pyjokes
from django.shortcuts import render

def home(request):
    joke = pyjokes.get_joke()
    return render(request, 'main/index.html', {'joke': joke})