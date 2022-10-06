from django.contrib import admin
from .models import Article


from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Article, ArticleAdmin)