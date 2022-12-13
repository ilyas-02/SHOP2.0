from django.contrib import admin
from .models import Category, Clothes, Brand, ClothesColor, ClothesSize, ClothesInStock


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('id', 'clothes_name', 'clothes_price', 'clothes_type', 'clothes_brand', 'clothes_category')
    list_filter = ('clothes_type', 'clothes_brand', 'clothes_category')
    prepopulated_fields = {'clothes_slug': ('clothes_name',)}
    search_fields = ('clothes_name', 'clothes_description', 'clothes_brand__brand_name', 'clothes_category__category_name')
    list_display_links = ('id', 'clothes_name')
    list_select_related = ('clothes_brand', 'clothes_category',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'brand_slug')
    list_display_links = ('id', 'brand_name')
    search_fields = ('brand_name', 'brand_description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('id', 'category_name', 'category_description')
    list_display_links = ('id', 'category_name')
    prepopulated_fields = {'category_slug': ('category_name',)}


class ClothesColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'color_name', 'color_slug')
    list_display_links = ('id', 'color_name')
    prepopulated_fields = {'color_slug': ('color_name',)}
    search_fields = ('color_name', 'color_slug')


class ClothesSizeAdmin(admin.ModelAdmin):
    list_display = ('ch', 'eu', 'us', )
    search_fields = ('ch', 'eu', 'us', )
    list_display_links = ('ch', 'eu', 'us', )


class ClothesInStockAdmin(admin.ModelAdmin):
    list_display = ('id', 'clothes', 'clothes_size', 'clothes_color', 'clothes_count')
    list_display_links = ('id', 'clothes')
    search_fields = ('clothes__clothes_name',)
    list_filter = ('clothes', )
    list_select_related = ('clothes', 'clothes_size', 'clothes_color', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ClothesSize, ClothesSizeAdmin)
admin.site.register(ClothesColor, ClothesColorAdmin)
admin.site.register(ClothesInStock, ClothesInStockAdmin)

# Register your models here.
