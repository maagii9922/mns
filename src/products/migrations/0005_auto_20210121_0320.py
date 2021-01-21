# Generated by Django 3.1.2 on 2021-01-21 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210104_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Арьс арчилгаа', 'Арьс арчилгаа'), ('Хямдралтай', 'Хямдралтай'), ('Үс арчилгаа', 'Үс арчилгаа'), ('Бие арчилгаа', 'Бие арчилгаа'), ('Гар арчилгаа', 'Гар арчилгаа'), ('Санитас ариутгагч', 'Санитас ариутгагч'), ('Хүүхэд', 'Хүүхэд'), ('Мойл органик', 'Мойл органик'), ('Мойл спа', 'Мойл спа')], default='', max_length=550, verbose_name='Ангилал'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, default='0', max_length=10, null=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Тайлбар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Хямдрал'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/product/', verbose_name='Зураг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Нэр'),
        ),
        migrations.AlterField(
            model_name='product',
            name='point',
            field=models.IntegerField(blank=True, default=5, null=True, verbose_name='Оноо'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Үнэ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Үлдэгдэл'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(blank=True, null=True, verbose_name='Үнэлгээ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbimage',
            field=models.ImageField(upload_to='media/productthumb/', verbose_name='Зураг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='variation',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.variation'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Зураг'),
        ),
    ]
