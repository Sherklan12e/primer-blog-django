from django.contrib import admin
from django.urls import path
from .views import upload_video, videos

app_name = 'videos'
urlpatterns = [
    path('videos/upload/', upload_video, name='upload_video'),
    path('videos/', videos, name='videos'),
]



