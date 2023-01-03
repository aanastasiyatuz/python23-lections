"================admin.py================"
# admin.py - файл, который отвечает за отображение моделей в админской панели

# простое отображение модели
"""
from django.contrib import admin
from .models import Product

admin.site.register(Product)
"""

# если вы хотите улучшить отображение:
"""
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] # то что будет отображаться при листинге обьектов
    list_filter = ['title', 'price'] # поля, по которым будет проходить фильтрация обьектов
    search_fields = ['title', 'description'] # поля, по которым будет проходить поиск

admin.site.register(Product, ProductAdmin)
"""

# если есть связи, то можно подключить их отображение в главную модель
"""
from django.contrib import admin
from .models import Product, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]

admin.site.register(Product, ProductAdmin)
"""
