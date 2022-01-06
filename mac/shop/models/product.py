from django.db import models

from .category import Category

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    product_perice=models.IntegerField(default=0)
    product_date=models.DateTimeField(auto_now_add=True)
    product_image=models.ImageField(upload_to='product/image')
