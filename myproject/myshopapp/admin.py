from django.contrib import admin
from .models import ProductModel, CustomerModel, OrderModel, OrderDetailsModel


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'description']
    ordering = ['-quantity']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer']


# Register your models here.
admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(CustomerModel, CustomerModelAdmin)
admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(OrderDetailsModel)
