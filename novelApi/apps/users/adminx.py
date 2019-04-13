import xadmin
from xadmin import views
from .models import VerifyCode


class Title(object):
    site_title = '分享阅读管理系统'
    site_footer = '分享阅读网'
    menu_style = 'accordion'


class Theme(object):
    enable_themes = True
    use_bootswatch = True


class VerifyCodeAdmin(object):
    list_display = ('id', 'code', 'mobile', 'create_time')


xadmin.site.register(views.BaseAdminView, Theme)
xadmin.site.register(views.CommAdminView, Title)

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
