from django.db import models
from django.contrib.auth import get_user_model
from novels.models import Novel

User = get_user_model()


class Fav(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='作品', help_text='作品')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


class Like(models.Model):
    """
    点赞
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='作品', help_text='作品')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


class Cmt(models.Model):
    """
    评论
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='作品', help_text='作品')
    content = models.CharField(max_length=500, verbose_name='内容', help_text='内容')
    reply = models.ForeignKey('self', related_name='replys', on_delete=models.CASCADE, null=True, verbose_name='回复',
                              help_text='回复: 空(评论), 非空(回复)')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']


class History(models.Model):
    """
    历史记录
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='作品', help_text='作品')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    def __str__(self):
        return self.novel.title

    class Meta:
        verbose_name = '历史记录'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']
