from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count_product=0)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'date_registration', 'date_update']
    list_filter = ['name', 'date_registration']
    search_fields = ['name', 'address']
    date_hierarchy = 'date_registration'
    ordering = ['name', 'date_registration']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'count_product', 'date_added']
    list_filter = ['name', 'price', 'date_added']
    search_fields = ['name', 'description']
    date_hierarchy = 'date_added'
    ordering = ['price', 'date_added']
    actions = [reset_quantity]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']
    list_filter = ['customer', 'date_ordered']
    search_fields = ['customer']
    date_hierarchy = 'date_ordered'
    ordering = ['total_price', 'date_ordered']
