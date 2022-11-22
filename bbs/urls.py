from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from django.views.generic import TemplateView

app_name = 'bbs'

urlpatterns = [
  path('',cache_page(31557600)(views.index), name='index'),
  path('<slug:slug>/',cache_page(31557600)(views.detail), name='detail'),
  path('category/<str:category>/',cache_page(31557600)(views.category), name='category'),
  path('tag/<str:tag>/',cache_page(31557600)(views.tag), name='tag'), 
  path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]
