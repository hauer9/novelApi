from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import xadmin
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from novels.views import NovelViewSet, SliderViewSet, TypeViewSet, ChapterViewSet
from users.views import UserViewSet, LoginSmsCodeViewSet, RegSmsCodeViewSet
from operation.views import FavViewSet, LikeViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'novels', NovelViewSet, base_name='novels')
router.register(r'sliders', SliderViewSet, base_name='sliders')
router.register(r'types', TypeViewSet, base_name='types')
router.register(r'chapters', ChapterViewSet, base_name='chapters')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'logincodes', LoginSmsCodeViewSet, base_name='logincodes')
router.register(r'regcodes', RegSmsCodeViewSet, base_name='regcodes')
router.register(r'favs', FavViewSet, base_name='favs')
router.register(r'likes', LikeViewSet, base_name='likes')

urlpatterns = [
    path('admin', xadmin.site.urls),
    path('', include(router.urls)),
    path('login', obtain_jwt_token),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),
    path('doc', include_docs_urls(title='分享阅读网')),
    path('ckeditor', include('ckeditor_uploader.urls')),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)


