# Generated by Django 4.1.1 on 2022-11-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0009_alter_article_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail_image_webp',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル webp'),
        ),
    ]