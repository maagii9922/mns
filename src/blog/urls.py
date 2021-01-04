from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from src.blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("news/", views.blog_list, name="blog"),
    # path("news/<int:pk>", views.blog_detail),
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
