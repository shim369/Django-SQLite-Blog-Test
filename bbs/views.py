from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from bbs.models import Category, Article, Tag

def paginate_queryset(request, queryset, count):
  paginator = Paginator(queryset, count)
  page = request.GET.get('page')
  try:
      page_obj = paginator.page(page)
  except PageNotAnInteger:
      page_obj = paginator.page(1)
  except EmptyPage:
      page_obj = paginator.page(paginator.num_pages)
  return page_obj

def index(request):
  articles = Article.objects.order_by('-id')
  page_obj = paginate_queryset(request, articles, 9)
  return render(request,'bbs/index.html',{'articles': page_obj.object_list,'page_obj': page_obj})

def detail(request, slug):
  entries = Article.objects.order_by('-id')[:3]
  article = get_object_or_404(Article, slug=slug)
  return render(request,'bbs/detail.html',{'article': article,'entries': entries})

def category(request, category):
  category = Category.objects.get(name=category)
  articles = Article.objects.filter(category=category)
  return render(request, 'bbs/index.html',{'category': category, 'articles': articles })

def tag(request, tag):
  tag = Tag.objects.get(name=tag)
  articles = Article.objects.filter(tag=tag)
  return render(request, 'bbs/index.html', {'tag': tag, 'articles': articles })