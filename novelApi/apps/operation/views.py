from rest_framework import viewsets, mixins, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .models import Fav, Like
from .serializers import FavSerializer, LikeSerializer, FavDetailSerializer, LikeDetailSerializer


class FavViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = FavDetailSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'novel_id'

    def get_queryset(self):
        return Fav.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return FavSerializer
        return FavDetailSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        novel = instance.novel
        novel.fav_num += 1
        novel.save()

    def perform_destroy(self, instance):
        instance.delete()
        novel = instance.novel
        novel.fav_num -= 1
        novel.save()


class LikeViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = LikeDetailSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'novel_id'

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return LikeSerializer
        return LikeDetailSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        novel = instance.novel
        novel.like_num += 1
        novel.save()

    def perform_destroy(self, instance):
        instance.delete()
        novel = instance.novel
        novel.like_num -= 1
        novel.save()
