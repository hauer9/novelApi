from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Novel, Slider, Type, Tag, Chapter

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, label='标签', help_text='标签',
                                 error_messages={
                                     'max_length': '标签格式错误',
                                 })

    class Meta:
        model = Tag
        fields = ['name']


class ChapterCreateSerializer(serializers.ModelSerializer):
    chapter_title = serializers.CharField(max_length=50, allow_blank=False, label='章节名', help_text='章名',
                                          error_messages={
                                              'blank': '请输入章名',
                                              'required': '请输入章名',
                                              'max_length': '章名格式错误',
                                          })
    chapter_content = serializers.CharField(allow_blank=False, label='内容', help_text='内容',
                                            error_messages={
                                                'blank': '请输入内容',
                                                'required': '请输入内容',
                                            })

    class Meta:
        model = Chapter
        fields = ['novel', 'chapter_title', 'chapter_content']


class ChapterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class ChapterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['chapter_title', 'chapter_content']


class FirstChapterCreateSerializer(serializers.ModelSerializer):
    chapter_title = serializers.CharField(max_length=50, allow_blank=False, label='章节名', help_text='章名',
                                          error_messages={
                                              'blank': '请输入章名',
                                              'required': '请输入章名',
                                              'max_length': '章名格式错误',
                                          })
    chapter_content = serializers.CharField(allow_blank=False, label='内容', help_text='内容',
                                            error_messages={
                                                'blank': '请输入内容',
                                                'required': '请输入内容',
                                            })

    class Meta:
        model = Chapter
        fields = ['chapter_title', 'chapter_content']


class NovelsCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50, allow_blank=False, label='作品名', help_text='作品名',
                                  validators=[UniqueValidator(queryset=Novel.objects.all(), message='作品名已存在')],
                                  error_messages={
                                      'blank': '请输入作品名',
                                      'required': '请输入作品名',
                                      'max_length': '作品名格式错误',
                                  })
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    type = serializers.PrimaryKeyRelatedField(required=True, queryset=Type.objects.all())
    tags = serializers.CharField(label='标签', help_text='标签')
    chapter = FirstChapterCreateSerializer()

    class Meta:
        model = Novel
        fields = ['title', 'author', 'type', 'tags', 'chapter']


class NovelsUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50, allow_blank=False, label='标题', help_text='标题',
                                  validators=[UniqueValidator(queryset=Novel.objects.all(), message='标题已存在')],
                                  error_messages={
                                      'blank': '请输入标题',
                                      'required': '请输入标题',
                                      'max_length': '标题格式错误',
                                  })

    class Meta:
        model = Novel
        fields = ['title', 'type', 'tags', 'introduction', 'notice', 'cover', 'status']


class NovelsDetailSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()
    type = TypeSerializer()
    tags = TagSerializer(many=True)
    chapters = ChapterDetailSerializer(many=True)

    class Meta:
        model = Novel
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    novel = NovelsDetailSerializer()

    class Meta:
        model = Slider
        fields = '__all__'
