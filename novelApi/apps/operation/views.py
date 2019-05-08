from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework import viewsets, authentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .models import Fav, Like, Cmt, History, SearchRecord, Follow
from .serializers import FavCreateSerializer, LikeCreateSerializer, FavDetailSerializer, LikeDetailSerializer, \
    CmtCreateSerializer, CmtDetailSerializer, HistorySerializer, SearchRecordSerializer, SearchRecordCreateSerializer, \
    FollowCreateSerializer, FollowDetailSerializer
from .filter import HistoryFilter, SearchRecordFilter


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class FavViewSet(viewsets.ModelViewSet):
    serializer_class = FavDetailSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'novel_id'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('novel__title',)

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


class LikeViewSet(viewsets.ModelViewSet):
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


class CmtViewSet(viewsets.ModelViewSet):
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


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'novel_id'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = HistoryFilter

    def get_queryset(self):
        return History.objects.filter(user=self.request.user)


class SearchRecordViewSet(viewsets.ModelViewSet):
    serializer_class = SearchRecordSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = SearchRecordFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return SearchRecordCreateSerializer
        return SearchRecordSerializer

    def get_queryset(self):
        return SearchRecord.objects.filter(user=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowDetailSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    lookup_field = 'follower_id'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('follower__nickname',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return FollowCreateSerializer
        return FollowDetailSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        user = instance.user
        user.follow_num += 1
        user.save()

    def perform_destroy(self, instance):
        instance.delete()
        user = instance.user
        user.follow_num -= 1
        user.save()
