from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'currency')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_id')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('type', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'tax')

    # def view_items_count(self, obj):
    #     return format_html(f'<p>{obj.items.count()}</p>')

    # view_items_count.short_description = "Количество товаров в заказе"