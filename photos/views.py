from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Photo
from .forms import PhotoForm

# Create your views here.

def hello(request):
    return HttpResponse('안녕하세요!')


def detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    #try:
    #    photo = Photo.objects.get(pk=pk)
    #except Photo.DoseNotExist:
    #    return HttpResponse('no picture')

    msg = (
        '<p>{pk}번의 사진을 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(msg))


def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)


def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES, request.user)

        if edit_form.is_valid():
            new_photo = edit_form.save(commit=False)
            new_photo.user = request.user
            new_photo.save()

            return redirect(new_photo.get_absolute_url())
