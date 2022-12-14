# Generated by Django 4.1.1 on 2022-11-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリー')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='タグ')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='タイトル')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='説明')),
                ('content', models.TextField(verbose_name='テキスト')),
                ('article_body', models.CharField(max_length=3000, null=True, verbose_name='プレーンテキスト')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='更新日')),
                ('thumbnail_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル')),
                ('thumbnail_image_webp', models.ImageField(blank=True, null=True, upload_to='', verbose_name='サムネイル webp')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='スラッグ')),
                ('tag_image', models.CharField(max_length=200, null=True, verbose_name='タグ画像用')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bbs.category', verbose_name='カテゴリー')),
                ('tag', models.ManyToManyField(to='bbs.tag', verbose_name='タグ')),
            ],
        ),
    ]
