from django.contrib import admin
from .models import Sales, SaleItem

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1  # número de líneas extra para agregar

@admin.register(Sales)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total_price')  # columnas que se muestran en la lista de ventas
    inlines = [SaleItemInline]  # mostrar los SaleItems dentro del Sale

@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('sale', 'product', 'quantity', 'unit_price')
