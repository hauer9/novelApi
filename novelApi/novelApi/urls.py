from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import xadmin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from novels.views import NovelViewSet, SliderViewSet, TypeViewSet, TagViewSet, ChapterViewSet, extract_tags, RecommendViewSet
from users.views import UpdatePwdViewSet, CodeUpdatePwdViewSet, UserViewSet, SmsCodeViewSet, RegSmsCodeViewSet
from operation.views import FavViewSet, LikeViewSet, CmtViewSet, HistoryViewSet, SearchRecordViewSet, FollowViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'novels', NovelViewSet, base_name='novels')
router.register(r'recommends', RecommendViewSet, base_name='recommends')
router.register(r'sliders', SliderViewSet, base_name='sliders')
router.register(r'types', TypeViewSet, base_name='types')
router.register(r'tags', TagViewSet, base_name='tags')
router.register(r'chapters', ChapterViewSet, base_name='chapters')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'update_pwd', UpdatePwdViewSet, base_name='update_pwd')
router.register(r'code_update_pwd', CodeUpdatePwdViewSet, base_name='code_update_pwd')
router.register(r'codes', SmsCodeViewSet, base_name='codes')
router.register(r'reg_codes', RegSmsCodeViewSet, base_name='reg_codes')
router.register(r'favs', FavViewSet, base_name='favs')
router.register(r'likes', LikeViewSet, base_name='likes')
router.register(r'cmts', CmtViewSet, base_name='cmts')
router.register(r'historys', HistoryViewSet, base_name='historys')
router.register(r'search_records', SearchRecordViewSet, base_name='search_records')
router.register(r'follows', FollowViewSet, base_name='follows')

urlpatterns = [
    path('admin', xadmin.site.urls),
    path('', include(router.urls)),
    path('login', obtain_jwt_token),
    path('extract_tags', extract_tags),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('doc', include_docs_urls(title='分享阅读网')),
    path('ckeditor', include('ckeditor_uploader.urls')),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)


