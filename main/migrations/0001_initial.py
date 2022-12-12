# Generated by Django 3.2 on 2022-12-07 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, verbose_name='Название')),
                ('brand_description', models.TextField(verbose_name='Описание')),
                ('brand_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Название')),
                ('category_description', models.TextField(verbose_name='Описание')),
                ('category_slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_name', models.CharField(max_length=100, verbose_name='Название')),
                ('clothes_description', models.TextField(verbose_name='Описание')),
                ('clothes_slug', models.SlugField(max_length=100, unique=True)),
                ('clothes_type', models.CharField(choices=[('man', 'Мужской'), ('woman', 'Женский'), ('kid', 'Детский'), ('uni', 'Универсальный')], max_length=100, verbose_name='Тип')),
                ('clothes_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('clothes_image', models.ImageField(upload_to='clothes', verbose_name='Картинка')),
                ('clothes_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.brand', verbose_name='Бренд')),
                ('clothes_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='main.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Одежда',
                'verbose_name_plural': 'Одежды',
            },
        ),
    ]