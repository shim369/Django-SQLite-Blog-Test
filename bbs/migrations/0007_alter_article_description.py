# Generated by Django 4.1.1 on 2022-10-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='説明'),
        ),
    ]
