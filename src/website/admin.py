from django.contrib import admin

from src.website.models import (
    Banner,
    Feedback,
    Influencer,
    MonthlyProduct,
    SaleProduct,
    btn,
    animationClass,
    introductionOne,
    MonProducts
)


from src.products.models import (
    Product
)

# Register your models here.

admin.site.register(Banner)
admin.site.register(btn)
admin.site.register(animationClass)
admin.site.register(introductionOne)
admin.site.register(MonthlyProduct)
admin.site.register(SaleProduct)
admin.site.register(Influencer)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]


admin.site.register(Feedback, FeedbackAdmin)


class MonProductsAdmin(admin.ModelAdmin):
    filter_horizontal = ['product']

admin.site.register(MonProducts, MonProductsAdmin)

