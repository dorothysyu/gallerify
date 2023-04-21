from django.conf.urls import include, url
# from .views import GalleryView
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(prefix=r'item', viewset=ItemViewSet, basename='item')

# urlpatterns = [
#     path(r'^api/', include(router.urls)) ,
#     url(r'^admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', views.index),
    path('spotify/', views.spotify),
]