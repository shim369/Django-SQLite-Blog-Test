from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'bbs'

urlpatterns = [
  path('',views.index, name='index'),
  path('<slug:slug>/',views.detail, name='detail'),
  path('category/<str:category>/', views.category, name='category'),
  path('tag/<str:tag>/', views.tag, name='tag'), 
  path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]
