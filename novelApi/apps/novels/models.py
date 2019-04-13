from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Type(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=8, verbose_name='类型', help_text='类型')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name


class Novel(models.Model):
    """
    作品属性
    """
    title = models.CharField(max_length=50, verbose_name='作品名', help_text='作品名')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', help_text='作者', related_name='novels')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='类型', help_text='类型')
    introduction = models.CharField(max_length=500, null=True, blank=True, verbose_name='简介', help_text='简介')
    cover = models.URLField(null=True, blank=True, default='http://qiniu.tuscanyyy.top/cover', verbose_name='封面', help_text='封面')
    notice = models.CharField(max_length=500, null=True, blank=True, verbose_name='公告', help_text='公告')
    status = models.BooleanField(default=False, verbose_name='状态', help_text='状态')
    click_num = models.PositiveIntegerField(default=0, verbose_name='点击数量', help_text='点击数量')
    fav_num = models.PositiveIntegerField(default=0, verbose_name='喜欢数量', help_text='喜欢数量')
    like_num = models.PositiveIntegerField(default=0, verbose_name='点赞数量', help_text='点赞数量')
    cmt_num = models.PositiveIntegerField(default=0, verbose_name='评论数量', help_text='评论数量')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '作品'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


class Chapter(models.Model):
    """
    章节
    """
    novel = models.ForeignKey(Novel, related_name='chapters', on_delete=models.CASCADE, verbose_name='作品',
                              help_text='作品')
    chapter_title = models.CharField(max_length=50, verbose_name='章名', help_text='章名')
    chapter_num = models.PositiveIntegerField(default=1, verbose_name='章数', help_text='章数')
    chapter_content = RichTextUploadingField(verbose_name='内容', help_text='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    def __str__(self):
        return self.chapter_title

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name


class Slider(models.Model):
    """
    轮播图
    """
    novel = models.OneToOneField(Novel, on_delete=models.CASCADE, verbose_name='作品', help_text='作品')
    slider = models.URLField(null=True, blank=True, verbose_name='轮播图', help_text='轮播图')

    def __str__(self):
        return self.novel.title

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
