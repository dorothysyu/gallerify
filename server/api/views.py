import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse, FileResponse
from api.models import Item
from server.server import Spotify
from server.render_gallery import Gallery
    
def index(request):
    return HttpResponse("hellooo")

def spotify(request):
    sp = Spotify()
    return JsonResponse(sp.albums_info, safe=False)

def draw_gallery(request):
    gallery = Gallery(Spotify().albums_info)
    gallery.draw()
    img = open('images/test_img.jpg', 'rb')
    response = FileResponse(img)
    return response

def draw_group(request):
    gallery = Gallery(Spotify().albums_info)
    gallery.draw_group()
    img = open('images/test_img2.jpg', 'rb')
    response = FileResponse(img)
    return response