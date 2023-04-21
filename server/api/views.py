import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from api.models import Item
from server.server import Spotify
    
def index(request):
    return HttpResponse("hellooo")

def spotify(request):
    sp = Spotify()
    return JsonResponse(sp.albums_info, safe=False)

# def draw_spotify(request):
#     sp = Spotify()
#     return HttpResponse(render_gallery(sp.albums_info))
