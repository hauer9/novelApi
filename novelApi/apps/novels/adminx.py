import xadmin
from .models import Novel, Type, Slider, Chapter


class NovelAdmin(object):
    list_display = (
        'id', 'title', 'author', 'click_num', 'like_num', 'fav_num', 'cmt_num', 'status', 'create_time',
        'last_update_time')


class TypeAdmin(object):
    list_display = ('id',)


class SliderAdmin(object):
    list_display = ('id', 'novel', 'slider')


class ChapterAdmin(object):
    list_display = ('id', 'novel', 'chapter_title', 'chapter_num', 'create_time', 'last_update_time')


xadmin.site.register(Novel, NovelAdmin)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Slider, SliderAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
