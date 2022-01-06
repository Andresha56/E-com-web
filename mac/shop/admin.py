from django.contrib import admin

from .models import product

from .models import category

from .models import Customer
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_date','product_category','product_image']


class CustomerAdmin(admin.ModelAdmin):
    list_display=['f_name','l_name','email']


admin.site.register(product.Product,ProductAdmin)


admin.site.register(category.Category)

admin.site.register(Customer,CustomerAdmin)

