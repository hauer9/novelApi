from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from novels.serializers import NovelsDetailSerializer
from .models import Fav, Like


class FavSerializer(serializers.ModelSerializer):
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


class LikeSerializer(serializers.ModelSerializer):
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
