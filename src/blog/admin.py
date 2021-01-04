from django.contrib import admin
from src.blog.models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "category"]


admin.site.register(Blog, BlogAdmin)