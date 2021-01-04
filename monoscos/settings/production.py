from .common import *

DEBUG = False
ALLOWED_HOSTS = [
    "10.0.0.139",
    "localhost",
    "127.0.0.1",
    "www.monoscosmetics.mn",
    "admin.monoscosmetics.mn",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "monoscosmetics",
        "USER": "cosmeticuser",
        "PASSWORD": "cosmeticuser",
        "HOST": "localhost",
        "PORT": "5432",
    }
}