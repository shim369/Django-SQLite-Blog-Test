# Generated by Django 4.1.1 on 2022-10-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
