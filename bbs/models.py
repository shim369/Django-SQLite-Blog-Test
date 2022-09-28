from django.db import models

# 投稿内容を格納するモデルを定義
class Article(models.Model):
  content = models.CharField(max_length=200)

  def __str__(self):
    return self.content