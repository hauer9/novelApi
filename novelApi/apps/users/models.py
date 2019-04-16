from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    gender_choices = ((0, '男'), (1, '女'), (2, '保密'),)

    mobile = models.CharField(max_length=11, verbose_name='电话', help_text='电话')
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name='昵称', help_text='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日', help_text='生日')
    gender = models.IntegerField(choices=gender_choices, default=2, verbose_name='性别',
                                 help_text='性别: 0(男), 1(女), 2(保密)')
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='邮箱', help_text='邮箱')
    avatar = models.URLField(null=True, blank=True, default='qiniu.tuscanyyy.top/avatar',
                             verbose_name='头像', help_text='头像')
    is_verified = models.BooleanField(default=False, verbose_name='是否认证', help_text='是否认证')
    follows = models.ManyToManyField('self', blank=True, related_name='follows', verbose_name='关注的人', help_text='关注的人')

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=6, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name
