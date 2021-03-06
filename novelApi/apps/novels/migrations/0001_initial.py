# Generated by Django 2.1.8 on 2019-04-01 23:26

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_title', models.CharField(help_text='章名', max_length=50, verbose_name='章名')),
                ('chapter_num', models.PositiveIntegerField(default=1, help_text='章数', verbose_name='章数')),
                ('chapter_content', ckeditor_uploader.fields.RichTextUploadingField(help_text='内容', verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('last_update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='作品名', max_length=50, verbose_name='作品名')),
                ('introduction', models.CharField(blank=True, help_text='简介', max_length=500, null=True, verbose_name='简介')),
                ('cover', models.URLField(blank=True, default='http://po23edlo8.bkt.clouddn.com/cover', help_text='封面', null=True, verbose_name='封面')),
                ('notice', models.CharField(blank=True, help_text='公告', max_length=500, null=True, verbose_name='公告')),
                ('status', models.BooleanField(default=False, help_text='状态', verbose_name='状态')),
                ('click_num', models.PositiveIntegerField(default=0, help_text='点击数量', verbose_name='点击数量')),
                ('fav_num', models.PositiveIntegerField(default=0, help_text='喜欢数量', verbose_name='喜欢数量')),
                ('like_num', models.PositiveIntegerField(default=0, help_text='点赞数量', verbose_name='点赞数量')),
                ('cmt_num', models.PositiveIntegerField(default=0, help_text='评论数量', verbose_name='评论数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('last_update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '作品',
                'verbose_name_plural': '作品',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider', models.URLField(blank=True, help_text='轮播图', null=True, verbose_name='轮播图')),
                ('novel', models.OneToOneField(help_text='作品', on_delete=django.db.models.deletion.CASCADE, to='novels.Novel', verbose_name='作品')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='类型', max_length=8, verbose_name='类型')),
            ],
            options={
                'verbose_name': '类型',
                'verbose_name_plural': '类型',
            },
        ),
    ]
