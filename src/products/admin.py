from django.contrib import admin
from src.products.models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)