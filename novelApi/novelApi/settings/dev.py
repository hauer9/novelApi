from .base import *

SECRET_KEY = 'j!l02#zh@fi^e$1-xd9+^u$nkl1i0i+*q$)(=wqou+hpbc8+-t'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'novel',
        'USER': 'root',
        'PASSWORD': 'asd.0399',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# redis缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "asd.03",
        }
    }
}

# 云片
API_KEY = 'abe1faed262c5e6ef5a7ef8b75927e52'

# 七牛
AK = 'DFRR7hd_lEoILDjPw2rRF6EpHAw1-qKVQHRpCEoT'
SK = 'Uu7hsdlfDITJReT_RuTQczYIEUEnbi78wSQpMTOh'
BUCKET = 'tuscany'
QINIU_API = 'qiniu.tuscanyyy.top'
