from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

from novels.serializers import NovelsDetailSerializer
from .models import Fav, Like, Cmt, History, SearchRecord, Follow

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FavCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Fav
        fields = ('id', 'user', 'novel')
        validators = [
            UniqueTogetherValidator(
                queryset=Fav.objects.all(),
                fields=('user', 'novel'),
                message='已经收藏'
            )
        ]


class FavDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    novel = NovelsDetailSerializer()

    class Meta:
        model = Fav
        fields = ('user', 'novel')


class OtherDetailSerializer(serializers.ModelSerializer):
    novels = NovelsDetailSerializer(many=True)
    favs = FavDetailSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'mobile', 'email', 'gender', 'nickname', 'date_joined', 'follow_num', 'is_verified', 'avatar',
                  'bgc', 'novels', 'favs']


class LikeCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = ('id', 'user', 'novel')
        validators = [
            UniqueTogetherValidator(
                queryset=Like.objects.all(),
                fields=('user', 'novel'),
                message='已经点赞'
            )
        ]


class LikeDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    novel = NovelsDetailSerializer()

    class Meta:
        model = Like
        fields = ('user', 'novel')


class CmtCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    content = serializers.CharField(max_length=500, allow_blank=False, label='内容', help_text='内容',
                                    error_messages={
                                        'blank': '请输入内容',
                                        'required': '请输入内容',
                                        'max_length': '内容格式错误',
                                    })

    class Meta:
        model = Cmt
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Cmt
        fields = '__all__'


class CmtDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    replys = ReplySerializer(many=True)

    class Meta:
        model = Cmt
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    novel = NovelsDetailSerializer()

    class Meta:
        model = History
        fields = '__all__'


class SearchRecordCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SearchRecord
        fields = ('id', 'user', 'content')


class SearchRecordSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    content = serializers.CharField(max_length=100, allow_blank=False, label='内容', help_text='内容',
                                    error_messages={
                                        'blank': '请输入内容',
                                        'required': '请输入内容',
                                        'max_length': '内容格式错误',
                                    })

    class Meta:
        model = SearchRecord
        fields = '__all__'


class FollowCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Follow
        fields = ('id', 'user', 'follower')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'follower'),
                message='已经关注'
            )
        ]


class FollowDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    follower = OtherDetailSerializer()

    class Meta:
        model = Follow
        fields = ('user', 'follower')
