from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from bbs.models import Category,Article

def index(request):
  Entries = Article.objects.all()[:3]
  articles = Article.objects.all()
  context = {
      'message': 'Welcom my Diary',
      'articles': articles,
      'Entries': Entries,
    }
  return render(request,'bbs/index.html',context)
  # return HttpResponse('Hello Django')

def detail(request, slug):
  Entries = Article.objects.all()[:3]
  article = get_object_or_404(Article, slug=slug)
  context = {
    'article': article,
    'Entries': Entries,
  }
  return render(request,'bbs/detail.html',context)

def category(request, category):
    category = Category.objects.get(name=category)
    articles = Article.objects.filter(category=category)
    return render(request, 'bbs/index.html',
                   {'category': category, 'articles': articles })

