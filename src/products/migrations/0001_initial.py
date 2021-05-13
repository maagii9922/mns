# Generated by Django 3.1.2 on 2021-05-13 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255, null=True, verbose_name='Өнгө')),
                ('colorCode', models.CharField(max_length=255, null=True, verbose_name='Код')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Зураг')),
            ],
            options={
                'verbose_name': 'Сонголт',
                'verbose_name_plural': 'Сонголт',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('БИОГЕН', 'Биоген'), ('БИОМОН', 'Биомон'), ('БИОДЕРМ', 'Биодерм'), ('АЛОЕ', 'Алое'), ('САНИТАС', 'Санитас')], default='', max_length=550)),
                ('brand_en', models.CharField(choices=[('BIOGEN', 'Biogen'), ('BIOMEN', 'Biomon'), ('BIODERM', 'Bioderm'), ('ALOE', 'Aloe'), ('SANITAS', 'Sanitas')], default='', max_length=550)),
                ('category', models.CharField(choices=[('Арьс арчилгаа', 'Арьс арчилгаа'), ('Хямдралтай', 'Хямдралтай'), ('Үс арчилгаа', 'Үс арчилгаа'), ('Бие арчилгаа', 'Бие арчилгаа'), ('Гар арчилгаа', 'Гар арчилгаа'), ('Санитас ариутгагч', 'Санитас ариутгагч'), ('Хүүхэд', 'Хүүхэд'), ('Мойл органик', 'Мойл органик'), ('Мойл спа', 'Мойл спа')], default='', max_length=550, verbose_name='Ангилал')),
                ('category_en', models.CharField(choices=[('Skin', 'Skin'), ('Sale', 'Sale'), ('Үс арчилгаа', 'Үс арчилгаа'), ('Бие арчилгаа', 'Бие арчилгаа'), ('Гар арчилгаа', 'Гар арчилгаа'), ('Санитас ариутгагч', 'Санитас ариутгагч'), ('Хүүхэд', 'Хүүхэд'), ('Мойл органик', 'Мойл органик'), ('Мойл спа', 'Мойл спа')], default='', max_length=550, verbose_name='Ангилал_en')),
                ('code', models.CharField(blank=True, default='0', max_length=10, null=True, verbose_name='Код')),
                ('image', models.ImageField(upload_to='media/product/', verbose_name='Зураг')),
                ('name', models.CharField(max_length=50, verbose_name='Нэр')),
                ('name_en', models.CharField(max_length=50, verbose_name='Нэр_en')),
                ('point', models.IntegerField(blank=True, default=5, null=True, verbose_name='Оноо')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Үнэ')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='Үнэлгээ')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Үлдэгдэл')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Хямдрал')),
                ('thumbimage', models.ImageField(upload_to='media/productthumb/', verbose_name='Зураг')),
                ('description', models.TextField(verbose_name='Тайлбар')),
                ('description_en', models.TextField(verbose_name='Тайлбар_en')),
                ('slug', models.SlugField()),
                ('link_to_emonos', models.CharField(blank=True, max_length=500, null=True, verbose_name='Имонос линк')),
                ('variation', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.variation')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүн',
                'verbose_name_plural': 'Бүтээгдэхүүн',
                'ordering': ['id'],
            },
        ),
    ]
