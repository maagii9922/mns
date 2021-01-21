from django.db import models
from django.db.models.aggregates import Max
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.


class MonthSaleProduct(models.Model):
    picture = models.ImageField(upload_to="media/salemonthproduct")
    alt_text = models.CharField(verbose_name=_("Зургын нэр"), max_length=255)
    order = models.IntegerField(verbose_name=_("Эрэмблэх дараалал"))

    class Meta:
        verbose_name = _("Сарын онцлох бүтээгдэхүүн")
        verbose_name_plural = _("Сарын онцлох бүтээгдэхүүн")
        ordering = ["order"]

    def __str__(self):
        return self.alt_text


class Influencer(models.Model):
    name = models.CharField(verbose_name=_("Нэр"), max_length=255)
    image = models.ImageField(upload_to="media/influencer")
    position = models.CharField(verbose_name=_("Ажлын байр"), max_length=255)
    order = models.IntegerField(verbose_name=_("Эрэмблэх дараалал"))
    quote = models.CharField(
        verbose_name=_("Хэлсэн үг (Шаарлаггүй талбар)"), max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Олны танил хүмүүс")
        verbose_name_plural = _("Олны танил хүмүүс")
        ordering = ["order"]

    def __str__(self):
        return self.name


class btn(models.Model):
    content = models.CharField(
        max_length=55, null=True, blank=True, default="Appointment"
    )
    color = models.CharField(max_length=10, null=True, blank=True, default="red")

    class Meta:
        verbose_name = _("Баннер туслах товч")
        verbose_name_plural = _("Баннер туслах товч")

class animationClass(models.Model):
    title = models.CharField(
        max_length=255, null=True, blank=True, default="slider-one-title"
    )
    subtitle = models.CharField(
        max_length=255, null=True, blank=True, default="slider-one-subtitle"
    )
    button = models.CharField(
        max_length=255, null=True, blank=True, default="slider-one-button"
    )

    class Meta:
        verbose_name = _("Баннер туслах хэсэг")
        verbose_name_plural = _("Баннер туслах хэсэг")
class Banner(models.Model):
    title = models.CharField(max_length=1, null=True, blank=True)
    subTitle = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="media/banner", verbose_name=_("Зураг"))
    btn = models.ForeignKey(btn, on_delete=models.CASCADE)
    animationClass = models.ForeignKey(animationClass, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Баннер зураг")
        verbose_name_plural = _("Баннер зураг")


class introductionOne(models.Model):
    title = models.CharField(
        max_length=1000, verbose_name=_("Гарчиг")
    )
    description = RichTextField(verbose_name=_("Тайлбар"))
    photo = models.ImageField(upload_to="media/introductionOne",verbose_name=_("Зураг"))

    class Meta:
        verbose_name = _("Танилцуулга бүтээгдэхүүн")
        verbose_name_plural = _("Танилцуулга бүтээгдхүүн")

    def __str__(self):
        return self.title


class Reclam(models.Model):
    title = models.CharField(verbose_name=_("Гарчиг"), max_length=255)
    video = models.CharField(verbose_name=_("Бичлэг"), max_length=255)
    order = models.IntegerField(verbose_name=_("Эрэмблэх дараалал"))

    class Meta:
        verbose_name = _("Реклам")
        verbose_name_plural = _("Реклам")


class MonthlyProduct(models.Model):
    image = models.ImageField(upload_to="media/monthly", verbose_name=_("Бүтээгдэхүүний зураг"))
    order = models.IntegerField(null=True, blank=True, verbose_name=_("Эрэмблэх дараалал"))

    class Meta:
        verbose_name = _("Сарын онцлох бүтээгдэхүүн")
        verbose_name_plural = _("Сарын онцлох бүтээгдэхүүн")
        ordering = ["-order"]


class SaleProduct(models.Model):
    image = models.ImageField(upload_to="media/monthly", null=True, blank=True, verbose_name=_("Бүтээгдэхүүний зураг"))
    order = models.IntegerField(null=True, blank=True, verbose_name=_("Эрэмблэх дараалал"))

    class Meta:
        verbose_name = _("Хямдралтай бүтээгдэхүүн")
        verbose_name_plural = _("Хямдралтай бүтээгдэхүүн")
        ordering = ["order"]


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Илгээгчийн нэр"))
    email = models.CharField(max_length=255, verbose_name=_("Имайл"))
    message = models.TextField()
    
    class Meta:
        verbose_name = _("Санал хүсэлт")
        verbose_name_plural = _("Санал хүсэлт")
        ordering = ["id"]
    
    def __str__(self):
        return self.name