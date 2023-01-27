from django.urls import path
# from .views import GalleryView
from .views import main

urlpatterns = [
    path('', main) #if we get a url, then call the GalleryView function from views.py
]
