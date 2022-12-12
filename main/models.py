from django.db import models

CLOTHES_TYPES = [
    ('man', 'Мужской'),
    ('woman', 'Женский'),
    ('kid', 'Детский'),
    ('uni', 'Универсальный'),
]

SEASON_TYPES = [
    ('winter', 'Зима'),
    ('spring', 'Весна'),
    ('summer', 'Лето'),
    ('autumn', 'Осень'),
]


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название')
    category_description = models.TextField(verbose_name='Описание')
    category_slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(verbose_name='Название', max_length=100)
    brand_description = models.TextField(verbose_name='Описание')
    brand_slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand_name


class Clothes(models.Model):
    clothes_name = models.CharField(verbose_name='Название', max_length=100)
    clothes_description = models.TextField(verbose_name='Описание')
    clothes_slug = models.SlugField(max_length=100, unique=True)
    clothes_type = models.CharField(verbose_name='Тип', max_length=100, choices=CLOTHES_TYPES)
    clothes_price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    clothes_image = models.ImageField(verbose_name='Картинка', upload_to='clothes', null=True, blank=True)
    clothes_brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.CASCADE,
                                      related_name='clothes', null=True, blank=True)
    clothes_category = models.ForeignKey(Category, verbose_name='Категории',
                                         on_delete=models.CASCADE, related_name='clothes')

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'

    def __str__(self):
        return self.clothes_name


class ClothesSize(models.Model):
    ch = models.CharField(max_length=10, verbose_name='Китайский размер')
    eu = models.CharField(max_length=10, verbose_name='европейский размер')
    us = models.CharField(max_length=10, verbose_name='Амерриеанский рразмер')

    def __str__(self):
        return self.ch

    def eu_size(self):
        return self.eu

    def us_size(self):
        return self.us

    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежд'


class ClothesColor(models.Model):
    color_name = models.CharField(max_length=100, verbose_name='Название цвета')
    color_slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = 'Цвет одежды'
        verbose_name_plural = 'Цвета одежд'


class ClothesInStock(models.Model):
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, related_name='clothes_in_stock')
    clothes_size = models.ForeignKey(ClothesSize, on_delete=models.CASCADE, related_name='clothes_in_stock')
    clothes_color = models.ForeignKey(ClothesColor, on_delete=models.CASCADE, related_name='clothes_in_stock')
    clothes_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.clothes}'

    class Meta:
        verbose_name = 'Одежда в наличии'
        verbose_name_plural = 'Одежда в наличии'






# Create your models here.
