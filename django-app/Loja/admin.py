from django.contrib import admin
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
    search_fields = ['name', 'price']
    list_filter = ['price']

admin.site.register(Products, ProductAdmin)

# Register your models here.
