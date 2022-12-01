from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from . import forms
from . import models
# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

#Функция для отображения моделек
def video_post(request):
    video_post = models.Video.objects.all()
    return render(request, 'video.html', {'post_video': video_post})
