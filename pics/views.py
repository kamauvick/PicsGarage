from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    images = Image.objects.all()
    print(str(images))
    return render(request, 'index.html', locals())


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET('image')
        searched_photos = Image.objects.filter(title__icontains=search_term)
        print(searched_photos)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'search_results.html', params)

    else:
        message = 'Ooppss, You did not search for anything.'
        return render(request, 'search_results.html', locals())
