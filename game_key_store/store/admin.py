from django.contrib import admin
from .models import Category, Product

# Регистрация моделей для отображения в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Поля для отображения
    search_fields = ('name',)  # Поле поиска по названию

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'category')  # Поля для отображения
    list_filter = ('category',)  # Фильтр по категории
    search_fields = ('name',)  # Поле поиска по названию
