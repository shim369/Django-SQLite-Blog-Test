from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from bbs.models import Category, Article, Tag

def index(request):
  articles = Article.objects.all()
  return render(request,'index.html',{'articles': articles})

def detail(request, slug):
  article = get_object_or_404(Article, slug=slug)
  return render(request,'detail.html',{'article': article})

def category(request, category):
  category = Category.objects.get(name=category)
  articles = Article.objects.filter(category=category)
  return render(request, 'index.html',{'category': category, 'articles': articles })

def tag(request, tag):
  tag = Tag.objects.get(name=tag)
  articles = Article.objects.filter(tag=tag)
  return render(request, 'index.html', {'tag': tag, 'articles': articles })