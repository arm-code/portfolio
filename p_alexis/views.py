from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def alexis(request):
    return render(request, 'profile.html', {} )

def test(request):
    return HTTPResponse(request, 'Hola mundo!!!')