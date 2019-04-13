import xadmin
from .models import Fav, Like


class FavAdmin(object):
    list_display = ('id', 'user', 'novel')


class LikeAdmin(object):
    list_display = ('id', 'user', 'novel')


xadmin.site.register(Fav, FavAdmin)
xadmin.site.register(Like, LikeAdmin)
