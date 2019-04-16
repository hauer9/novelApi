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
