# Generated by Django 4.1.1 on 2022-11-10 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail_image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='thumbnail_image_webp',
        ),
    ]
