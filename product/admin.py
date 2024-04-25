from django.contrib import admin
from .models import Product, ShopDetails, Category
from import_export.admin import ImportExportModelAdmin


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
    list_filter = ('category', 'description')
    search_fields = ('name',)
    list_display_links = ['name', 'price', 'category', 'description']


@admin.register(ShopDetails)
class ShopDetailsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'category', 'description')
    list_filter = ('category', 'description')
    search_fields = ('name',)
    list_display_links = ['name', 'price', 'category', 'description']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ['name', ]
