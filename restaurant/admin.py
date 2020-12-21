from django.contrib import admin
from .models import *

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at', 'restaurant']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','restaurant']

class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'restaurant','is_occupied']


class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table', 'status','restaurant','created_at']

class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ['id','food_order', 'food_option', 'status']

class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
class FoodExtraTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class FoodExtraAdmin(admin.ModelAdmin):
    list_display = ['id','name','food','price']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','name','restaurant','category']

class FoodOptionAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','food']

admin.site.register(Restaurant)
admin.site.register(Subscription)
admin.site.register(RestaurantContactPerson)
admin.site.register(RestaurantPromoCategory)

admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodOptionType)
admin.site.register(FoodExtraType, FoodExtraTypeAdmin)

admin.site.register(FoodExtra, FoodExtraAdmin)

admin.site.register(FoodOption, FoodOptionAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(FoodOrder,FoodOrderAdmin)
admin.site.register(OrderedItem, OrderedItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(PopUp)
admin.site.register(Slider)
