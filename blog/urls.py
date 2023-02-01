from django.contrib import admin
from django.urls import path
from .views import render_post, post_detail, render_about

app_name = 'blog'
urlpatterns = [
    path('', render_post, name='posts'),
    path('<int:post_id>', post_detail, name="post_detail"),
    path('about/', render_about, name='about' )
]
