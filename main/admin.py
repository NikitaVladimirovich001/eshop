from django.contrib import admin
from main.models import Product,Category, Country, Manufacturer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','count','garanty')
    search_fields = ('name',)
    fields = ('name','count','garanty','manufacturer','category')
    list_filter = ('garanty','count')

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','addres','phone_number')
    search_fields = ('name','addres','phone_number')
    fields = ('name','addres','phone_number')
