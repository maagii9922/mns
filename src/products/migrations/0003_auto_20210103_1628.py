# Generated by Django 3.1.2 on 2021-01-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201228_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Арьс арчилгаа', 'Арьс арчилгаа'), ('Хямдралтай', 'Хямдралтай'), ('Үс арчилгаа', 'Үс арчилгаа'), ('Бие арчилгаа', 'Бие арчилгаа'), ('Гар арчилгаа', 'Гар арчилгаа'), ('Санитас ариутгагч', 'Санитас ариутгагч'), ('Хүүхэд', 'Хүүхэд'), ('Мойл органик', 'Мойл органик'), ('Мойл спа', 'Мойл спа')], default='', max_length=550),
        ),
    ]