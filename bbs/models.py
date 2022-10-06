from turtle import title
from django.db import models

# 投稿内容を格納するモデルを定義
class Article(models.Model):
  title = models.CharField('タイトル', max_length=200, null=True)
  description = models.CharField('説明', max_length=500, null=True)
  content = models.TextField('テキスト')
  created_at = models.DateField('作成日', auto_now_add=True)
  updated_at = models.DateField('更新日', auto_now=True)
  thumbnail_image = models.ImageField(null=True, blank=True)


  def __str__(self):
    return self.title