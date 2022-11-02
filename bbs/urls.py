from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
  path('',views.index, name='index'),
  path('category/<str:category>/', views.category, name='category'),
  path('tag/<str:tag>/', views.tag, name='tag'), 
  path('<slug:slug>/',views.detail, name='detail'),
]
