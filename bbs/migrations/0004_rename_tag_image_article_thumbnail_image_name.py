# Generated by Django 4.1.1 on 2023-01-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_tag_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tag_image',
            new_name='thumbnail_image_name',
        ),
    ]
