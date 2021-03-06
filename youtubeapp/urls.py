from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'youtubeapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('video/<int:video_id>', views.show, name="show"),
    path('search/', views.search, name="search"),
    path('upload/', views.upload, name="upload"),
    path('upload_selesai/', views.upload_selesai, name="upload_selesai"),
    path('trending/', views.trending, name="trending")
]