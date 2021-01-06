from .common import *

DEBUG = True
ALLOWED_HOSTS = [
    "10.0.0.139",
    "localhost",
    "127.0.0.1",
    "www.monoscosmetics.mn",
    "admin.monoscosmetics.mn",
    "monoscosmetics.mn",
]

CORS_ORIGIN_WHITELIST = (
    "https://monoscosmetics.mn/",
    "http://10.0.0.153",
    "http://localhost:5005",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "monoscosmetics",
        "USER": "cosmeticuser",
        "PASSWORD": "#DiyjoT42u#M",
        "HOST": "localhost",
        "PORT": "5432",
    }
}