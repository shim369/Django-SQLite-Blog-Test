# Generated by Django 4.1.1 on 2022-12-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='スラッグ'),
        ),
    ]
