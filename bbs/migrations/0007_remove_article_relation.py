# Generated by Django 4.1.1 on 2022-11-02 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_alter_article_relation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='relation',
        ),
    ]
