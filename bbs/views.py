from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from bbs.models import Article

def index(request):
  articles = Article.objects.all()
  context = {
      'message': 'Welcom my Diary',
      'articles': articles,
    }
  return render(request,'bbs/index.html',context)
  # return HttpResponse('Hello Django')

def detail(request, slug):
  article = get_object_or_404(Article, slug=slug)
  context = {
    'article': article,
  }
  return render(request,'bbs/detail.html',context)

