# Generated by Django 4.1.1 on 2022-11-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0008_article_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_body',
            field=models.CharField(max_length=3000, null=True, verbose_name='プレーンテキスト'),
        ),
    ]
