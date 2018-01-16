from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Photo

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    messages = (
        '<p>{pk}번 사진</p>'.format(pk=photo.pk),
        '<p>주소: {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse(messages)
