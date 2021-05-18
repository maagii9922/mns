from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from src.products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("product/", views.product_list, name="product-list"),
    path("product/<int:pk>", views.product_detail),
    path("product/<category>", views.category_list),
    path("feedback", views.feedback, name="other-feedback"),
    url(r"^ckeditor/", include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
