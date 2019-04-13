from rest_framework import viewsets, status
from rest_framework import mixins, authentication, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from utils.permissions import IsAuthorOrReadOnly
from .models import Novel, Slider, Chapter, Type
from .serializers import NovelsCreateSerializer, NovelsDetailSerializer, NovelsUpdateSerializer, SliderSerializer, \
    TypeSerializer, ChapterCreateSerializer, ChapterDetailSerializer, ChapterUpdateSerializer


class NovelSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class ChapterViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ChapterDetailSerializer
    queryset = Chapter.objects.all()
    throttle_classes = (AnonRateThrottle, UserRateThrottle)

    def get_serializer_class(self):
        if self.action == 'create':
            return ChapterCreateSerializer
        elif self.action == 'update':
            return ChapterUpdateSerializer
        return ChapterDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        novel = serializer.validated_data['novel']
        chapter_title = serializer.validated_data['chapter_title']
        chapter_content = serializer.validated_data['chapter_content']
        chapter_num = Chapter.objects.filter(novel=novel).last().chapter_num + 1
        chapters = Chapter(novel=novel, chapter_title=chapter_title, chapter_num=chapter_num,
                           chapter_content=chapter_content)
        chapters.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class NovelViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = NovelsDetailSerializer
    queryset = Novel.objects.all()
    pagination_class = NovelSetPagination
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    throttle_classes = (AnonRateThrottle, UserRateThrottle)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsAuthorOrReadOnly()]
        elif self.action == 'update':
            return [permissions.IsAuthenticated(), IsAuthorOrReadOnly()]
        elif self.action == 'destroy':
            return [permissions.IsAuthenticated(), IsAuthorOrReadOnly()]
        return []

    def get_serializer_class(self):
        if self.action == 'create':
            return NovelsCreateSerializer
        elif self.action == 'update':
            return NovelsUpdateSerializer
        return NovelsDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data['title']
        author = serializer.validated_data['author']
        type = serializer.validated_data['type']
        chapter_title = serializer.validated_data['chapter']['chapter_title']
        chapter_content = serializer.validated_data['chapter']['chapter_content']

        novel = Novel(title=title, type=type, author=author)
        novel.save()
        chapters = Chapter(novel=novel, chapter_title=chapter_title, chapter_num=1, chapter_content=chapter_content)
        chapters.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('title',)
    filter_fields = ('type', 'status')
    ordering_fields = ('create_time', 'click_num', 'fav_num', 'like_num')


class SliderViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()


class TypeViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
