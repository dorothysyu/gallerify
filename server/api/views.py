from django.shortcuts import render
from rest_framework import generics
# from .models import Gallery
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("hello")