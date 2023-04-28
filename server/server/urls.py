from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from rest_framework import routers
from api import views

urlpatterns = [
    path('', views.index),
    path('spotify/', views.spotify),
    path('draw/', views.draw_gallery),
]