from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Photo
from .forms import PhotoForm

def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    messages = (
        '<p>{pk}번 사진</p>'.format(pk=photo.pk),
        '<p>주소: {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse(messages)


@login_required
def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }
    return render(request, 'edit.html', ctx)

