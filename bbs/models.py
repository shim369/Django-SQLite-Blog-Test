from turtle import title
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# 投稿内容を格納するモデルを定義
class Article(models.Model):
  title = models.CharField('タイトル', max_length=200, null=True)
  description = models.CharField('説明', max_length=500, null=True)
  content = models.TextField('テキスト')
  created_at = models.DateField('作成日', auto_now_add=True)
  updated_at = models.DateField('更新日', auto_now=True)
  thumbnail_image = models.ImageField('サムネイル',null=True, blank=True)
  slug = models.SlugField('スラッグ',blank=True, unique=False, max_length=255)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', args=[self.slug])

  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super(Article, self).save(*args, **kwargs)