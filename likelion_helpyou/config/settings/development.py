from .base import *

DEBUG = True

ALLOWED_HOSTS = ["halpyou.shop", "15.164.96.65"] # 도메인 ,ip;

DJANGO_APPS += [

]

PROJECT_APPS += [

]

THIRD_PARTY_APPS += [
    'mathfilters',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATICFILE_DIRS= [
    BASE_DIR / 'static'
]