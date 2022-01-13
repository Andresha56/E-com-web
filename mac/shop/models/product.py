from django.db import models

from .category import Category

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    product_perice=models.IntegerField(default=0)
    product_date=models.DateTimeField(auto_now_add=True)
    product_image=models.ImageField(upload_to='product/image')



    @staticmethod
    def get_product_by_product_category_id(product_category_id):
        if product_category_id:
            return Product.objects.filter(product_category=product_category_id)
        else:
            return Product.objects.all()