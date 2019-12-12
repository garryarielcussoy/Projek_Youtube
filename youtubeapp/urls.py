from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'youtubeapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('video/<int:video_id>', views.show, name="show")
]