from django.urls import path

from .views import search_video

urlpatterns = [
    path('',search_video),
]