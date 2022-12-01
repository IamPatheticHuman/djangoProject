from django.urls import path
from video import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('video_posts/', views.video_post, name='video_post'),

]