from django.db import models
from django.contrib.auth import get_user_model
from novels.models import Novel

User = get_user_model()


class Fav(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favs', verbose_name='用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='作品')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='用户')
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='作品')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
