from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    images = Image.objects.all()
    print(str(images))
    return render(request, 'index.html', locals())


def search_results(request):
    if 'photo' in request.GET and request.GET['photo']:
        search_term = request.GET('photo')
        searched_photos = Image.search_by_title(search_term)
        message = f'Search Term:{search_term}'

        return render(request, 'index.html', locals())

    else:
        message = 'Ooppss, You did not search for anything.'
        return render(request, 'index.html', locals())
