# Create your models here.

from django.db import models

# Create your models here.
CATEGORY_CHOICE = (
    ('АРЬС АРЧИЛГАА', 'Арьс арчилгаа'),
    ('ХЯМДРАЛТАЙ', 'Хямдралтай'),
    ('ҮС АРЧИЛГАА', 'Үс арчилгаа'),
)
BRAND_CHOICE = (
    ('БИОГЕН', 'Биоген'),
    ('БИОМОН', 'Биомон'),
    ('БИОДЕРМ', 'Биодерм'),
)
class Product(models.Model):
    category = models.CharField(max_length=550, choices=CATEGORY_CHOICE, default="")
    name = models.CharField(max_length=50)
    rate = models.IntegerField(null=True)
    price = models.IntegerField(null=False)
    discount = models.CharField(max_length=255, default="0")
    brand = models.CharField(max_length=550, choices=BRAND_CHOICE, default="")
    point = models.CharField(max_length=255)
    quantity = models.CharField(max_length = 255)
    thumbimage = models.ImageField(upload_to = 'media/productthumb/')
    image = models.ImageField(upload_to = 'media/product/')
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

