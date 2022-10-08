from django.contrib import admin
from .models import  Product,Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    
class PfferAdmin(admin.ModelAdmin):
        list_display = ('code', 'discount')
    
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Offer, PfferAdmin )



