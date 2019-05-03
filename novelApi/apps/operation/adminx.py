import xadmin
from .models import Fav, Like, Cmt, History, SearchRecord


class FavAdmin(object):
    list_display = ('id', 'user', 'novel')


class LikeAdmin(object):
    list_display = ('id', 'user', 'novel')


class CmtAdmin(object):
    list_display = ('id', 'user', 'novel', 'content', 'reply')


class HistoryAdmin(object):
    list_display = ('id', 'user', 'novel', 'create_time', 'update_time')


class SearchRecordAdmin(object):
    list_display = ('id', 'user', 'content', 'create_time', 'update_time')


xadmin.site.register(Fav, FavAdmin)
xadmin.site.register(Like, LikeAdmin)
xadmin.site.register(Cmt, CmtAdmin)
xadmin.site.register(History, HistoryAdmin)
xadmin.site.register(SearchRecord, SearchRecordAdmin)
