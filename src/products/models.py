# Create your models here.

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
CATEGORY_CHOICE = (
    ("Арьс арчилгаа", "Арьс арчилгаа"),
    ("Хямдралтай", "Хямдралтай"),
    ("Үс арчилгаа", "Үс арчилгаа"),
    ("Бие арчилгаа", "Бие арчилгаа"),
    ("Гар арчилгаа", "Гар арчилгаа"),
    ("Санитас ариутгагч", "Санитас ариутгагч"),
    ("Хүүхэд", "Хүүхэд"),
    ("Мойл органик", "Мойл органик"),
    ("Мойл спа", "Мойл спа"),
)
BRAND_CHOICE = (
    ("БИОГЕН", "Биоген"),
    ("БИОМОН", "Биомон"),
    ("БИОДЕРМ", "Биодерм"),
    ("АЛОЕ", "Алое"),
    ("САНИТАС", "Санитас"),
)


class variation(models.Model):
    color = models.CharField(verbose_name=_("Өнгө"), max_length=255, null=True)
    colorCode = models.CharField(verbose_name=_("Код"), max_length=255, null=True)
    image = models.ImageField(null=True)

    class Meta:
        verbose_name = _("Сонголт")
        verbose_name_plural = _("Сонголт")

    def __str__(self):
        return self.color


class Product(models.Model):
    brand = models.CharField(max_length=550, choices=BRAND_CHOICE, default="")
    category = models.CharField(max_length=550, choices=CATEGORY_CHOICE, default="")
    code = models.CharField(max_length=10, null=True, blank=True, default="0")
    description = models.TextField()
    image = models.ImageField(upload_to="media/product/")
    name = models.CharField(max_length=50)
    point = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    thumbimage = models.ImageField(upload_to="media/productthumb/")
    description = models.TextField()
    slug = models.SlugField()
    variation = models.ForeignKey(
        variation, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Бүтээгдэхүүн")
        verbose_name_plural = _("Бүтээгдэхүүн")
        ordering = ["id"]
        
    def __str__(self):
        return self.name
