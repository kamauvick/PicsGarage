from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^category/$', views.filter_by_category, name='category'),
    re_path(r'^location/$', views.filter_by_locale, name='locale'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
