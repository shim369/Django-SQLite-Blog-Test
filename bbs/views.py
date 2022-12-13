from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from bbs.models import Category, Article, Tag
from django.views.generic import TemplateView
# from django.views.generic import DetailView

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
	page_obj = paginate_queryset(request, articles, 6)
	return render(request,'bbs/index.html',{'articles': page_obj.object_list,'page_obj': page_obj})

def category(request, category):
	category = Category.objects.get(name=category)
	articles = Article.objects.order_by('-id').filter(category=category)
	page_obj = paginate_queryset(request, articles, 6)
	return render(request, 'bbs/list.html',{'category': category, 'articles': page_obj.object_list,'page_obj': page_obj })

def tag(request, tag):
	tag = Tag.objects.get(name=tag)
	articles = Article.objects.order_by('-id').filter(tag=tag)
	page_obj = paginate_queryset(request, articles, 6)
	return render(request, 'bbs/list.html',{'tag': tag, 'articles': page_obj.object_list,'page_obj': page_obj })
  
def detail(request, slug):
	entries = Article.objects.order_by('-id')[:3]
	article = get_object_or_404(Article, slug=slug)
	return render(request,'bbs/detail.html',{'article': article,'entries': entries})

def complete(request):
	entries = Article.objects.order_by('-id')[:3]
	article = Article.objects.order_by('-id')
	return render(request, 'bbs/complete.html', {'article':article,'entries': entries})

def contact_form(request):
	entries = Article.objects.order_by('-id')[:3]
	article = Article.objects.order_by('-id')
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			myself = form.cleaned_data['myself']
			recipients = [settings.EMAIL_HOST_USER]
			if myself:
				recipients.append(sender)
			try:
				send_mail(subject, message, sender, recipients)
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return redirect('bbs:complete')
	else:
		form = ContactForm()
	return render(request, 'bbs/contact.html', {'form': form,'article':article,'entries': entries})


def chart_data(request):
	article = Article.objects.order_by('-id')
	entries = Article.objects.order_by('-id')[:3]
	data = pd.read_csv("static/csv/weight - weight.csv")
	plt.figure(1)
	plt.plot(data['date'],data['weight'],marker="o")
	plt.xlabel('date')
	plt.ylabel('weight')
	plt.savefig('media/weight.png')
	return render(request, 'bbs/weight.html',{'article':article,'entries': entries})