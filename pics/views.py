from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    images = Image.objects.all()
    print(str(images))
    return render(request, 'index.html', locals())


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.search_by_title(search_term)
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


def filter_by_category(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.search_by_category(search_term)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'category.html', params)


def filter_by_locale(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.filter_by_location(search_term)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }
