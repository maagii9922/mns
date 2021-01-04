from django.contrib import admin
from src.products.models import Product, variation

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "category", "brand"]


admin.site.register(Product, ProductAdmin)
admin.site.register(variation)