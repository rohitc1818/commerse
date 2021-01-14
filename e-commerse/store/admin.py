from django.contrib import admin
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['First_name','Last_name','phone','email','password']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price','date','phone']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,OrderAdmin)
