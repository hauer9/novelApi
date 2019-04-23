from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status
from rest_framework import viewsets, mixins, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .models import Fav, Like, Cmt, History
from .serializers import FavCreateSerializer, LikeCreateSerializer, FavDetailSerializer, LikeDetailSerializer, \
    CmtCreateSerializer, CmtDetailSerializer, HistorySerializer


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
            return FavCreateSerializer
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
            return LikeCreateSerializer
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


class CmtViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CmtDetailSerializer
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    queryset = Cmt.objects.all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('novel',)

    # ordering_fields = ('create_time', 'click_num', 'fav_num', 'like_num')

    def get_serializer_class(self):
        if self.action == 'create':
            return CmtCreateSerializer
        return CmtDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def perform_create(self, serializer):
        instance = serializer.save()
        novel = instance.novel
        novel.cmt_num += 1
        novel.save()


class HistoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = HistorySerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'novel_id'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('update_time',)

    def get_queryset(self):
        return History.objects.filter(user=self.request.user)


