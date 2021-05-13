from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from src.website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("banner/", views.banner, name="banner"),
    path("introduction/", views.introduction, name="introduction"),
    path("monthly/", views.monthlyproduct, name="monthly"),
    path("influencer/", views.influencer, name="influencer"),
    path("saleproduct/", views.saleproduct, name="saleproduct"),
    # path("MonProduct/", views.monproduct, name="MonProduct"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
