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

CATEGORY_CHOICE_EN = (
    ("Skin", "Skin"),
    ("Sale", "Sale"),
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

BRAND_CHOICE_EN = (
    ("BIOGEN", "Biogen"),
    ("BIOMEN", "Biomon"),
    ("BIODERM", "Bioderm"),
    ("ALOE", "Aloe"),
    ("SANITAS", "Sanitas"),
)


class variation(models.Model):
    color = models.CharField(verbose_name=_("Өнгө"), max_length=255, null=True)
    colorCode = models.CharField(verbose_name=_("Код"), max_length=255, null=True)
    image = models.ImageField(null=True, verbose_name=_("Зураг"))

    class Meta:
        verbose_name = _("Сонголт")
        verbose_name_plural = _("Сонголт")

    def __str__(self):
        return self.color


class Product(models.Model):
    brand = models.CharField(max_length=550, choices=BRAND_CHOICE, default="")
    brand_en = models.CharField(max_length=550, choices=BRAND_CHOICE_EN, default="")
    category = models.CharField(
        max_length=550, choices=CATEGORY_CHOICE, default="", verbose_name=_("Ангилал")
    )
    category_en = models.CharField(
        max_length=550, choices=CATEGORY_CHOICE_EN, default="", verbose_name=_("Ангилал_en")
    )
    code = models.CharField(
        max_length=10, null=True, blank=True, default="0", verbose_name=_("Код")
    )
    description = models.TextField()
    image = models.ImageField(upload_to="media/product/", verbose_name=_("Зураг"))
    name = models.CharField(max_length=50, verbose_name=_("Нэр"))
    name_en = models.CharField(max_length=50, verbose_name=_("Нэр_en"))
    point = models.IntegerField(
        null=True, blank=True, default=5, verbose_name=_("Оноо")
    )
    price = models.IntegerField(null=True, blank=True, verbose_name=_("Үнэ"))
    rate = models.IntegerField(null=True, blank=True, verbose_name=_("Үнэлгээ"))
    quantity = models.IntegerField(null=True, blank=True, verbose_name=_("Үлдэгдэл"))
    discount = models.IntegerField(null=True, blank=True, verbose_name=_("Хямдрал"))
    thumbimage = models.ImageField(
        upload_to="media/productthumb/", verbose_name=_("Зураг")
    )
    description = models.TextField(verbose_name=_("Тайлбар"))
    description_en = models.TextField(verbose_name=_("Тайлбар_en"))
    slug = models.SlugField()
    variation = models.ForeignKey(
        variation, on_delete=models.CASCADE, null=True, blank=True, editable=False
    )
    link_to_emonos = models.CharField(
        null=True, blank=True, verbose_name=_("Имонос линк"), max_length=500
    )

    class Meta:
        verbose_name = _("Бүтээгдэхүүн")
        verbose_name_plural = _("Бүтээгдэхүүн")
        ordering = ["id"]

    def __str__(self):
        return self.name

