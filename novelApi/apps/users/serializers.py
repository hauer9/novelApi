from datetime import datetime, timedelta
import re

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.validators import UniqueValidator
from novels.serializers import NovelsDetailSerializer

from users.models import VerifyCode

User = get_user_model()


class LoginSmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text='手机号', error_messages={
        'blank': '请输入手机号',
        'required': '请输入手机号',
        'max_length': '手机号格式错误',
    })

    def validate_mobile(self, mobile):
        if not re.match(settings.MOBILE_REG, mobile):
            raise serializers.ValidationError('手机号码非法')

        if not User.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError('手机号码未注册')

        one_minutes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(create_time__gt=one_minutes_age, mobile=mobile).exists():
            raise serializers.ValidationError('距离上一次发送未超过60s')

        return mobile


class RegSmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, help_text='手机号', error_messages={
        'blank': '请输入手机号',
        'required': '请输入手机号',
        'max_length': '手机号格式错误',
    })

    def validate_mobile(self, mobile):
        if not re.match(settings.MOBILE_REG, mobile):
            raise serializers.ValidationError('手机号码非法')

        if User.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError('手机号码已被注册')

        one_minutes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(create_time__gt=one_minutes_age, mobile=mobile).exists():
            raise serializers.ValidationError('距离上一次发送未超过60s')

        return mobile


class UserRegSerialize(serializers.ModelSerializer):
    code = serializers.CharField(required=True, write_only=True, max_length=6, min_length=6, label='验证码',
                                 help_text='验证码',
                                 error_messages={
                                     'blank': '请输入验证码',
                                     'required': '请输入验证码',
                                     'max_length': '验证码格式错误',
                                     'min_length': '验证码不少于6个数字',
                                 })

    username = serializers.CharField(max_length=20, required=True, allow_blank=False, label='用户名', help_text='用户名',
                                     validators=[UniqueValidator(queryset=User.objects.all(), message='用户名已存在')],
                                     error_messages={
                                         'blank': '请输入用户名',
                                         'required': '请输入用户名',
                                         'max_length': '用户名格式错误',
                                     })

    mobile = serializers.CharField(max_length=11, required=True, allow_blank=False, label='电话', help_text='电话',
                                   validators=[UniqueValidator(queryset=User.objects.all(), message='手机号码已被注册')],
                                   error_messages={
                                       'blank': '请输入手机号',
                                       'required': '请输入手机号',
                                       'max_length': '手机号格式错误',
                                   })

    password = serializers.CharField(max_length=100, write_only=True, label='密码', help_text='密码',
                                     style={'input_type': 'password'},
                                     error_messages={
                                         'blank': '请输入密码',
                                         'required': '请输入密码',
                                         'max_length': '密码格式错误',
                                     })

    def create(self, validated_data):
        user = super(UserRegSerialize, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_code(self, code):
        last_record = VerifyCode.objects.filter(mobile=self.initial_data['mobile']).last()
        if last_record:
            five__minutes_age = datetime.now() - timedelta(hours=0, minutes=15, seconds=0)
            if five__minutes_age > last_record.create_time:
                raise serializers.ValidationError('验证码已过期')
            if last_record.code != code:
                raise serializers.ValidationError('验证码错误')
        else:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ['username', 'mobile', 'code', 'password']


class UserDetailSerializer(serializers.ModelSerializer):
    novels = NovelsDetailSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
