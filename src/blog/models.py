from django.db import models
from django.utils.translation import gettext as _
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

CATEGORY_CHOICES = [
    ("Онцлох мэдээ", "Онцлох мэдээ"),
    ("Зурган мэдээ", "Зурган мэдээ"),
    ("Бие арчилгаа", "Бие арчилгаа"),
    ("Мэдээ", "Мэдээ"),
]

TAG_CHOICES = [
    ("TR", "tricks"),
    ("MU", "make up"),
]


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Гарчиг"))
    description = models.CharField(max_length=500, verbose_name=_("Тайлбар"))
    content = RichTextUploadingField()
    author = models.CharField(
        max_length=55, verbose_name=_("Оруулсан админ"), default="Админ"
    )
    category = models.CharField(
        max_length=255,
        verbose_name=_("Ангилал"),
        choices=CATEGORY_CHOICES,
        default="МД",
    )
    tags = models.CharField(
        max_length=255, verbose_name=_("Шошго"), choices=TAG_CHOICES, default="TR"
    )
    publicDate = models.DateTimeField(auto_now_add=True)
    thumbImage = models.ImageField(upload_to="media/blog/thumbimage")
    coverImage = models.ImageField(upload_to="media/blog/coverimage")
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Мэдээ")
        verbose_name_plural = _("Мэдээ")
        ordering = ["-id"]