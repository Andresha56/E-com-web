


from django.db import models


class Category(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.category

    @staticmethod 
    def get_all_category():
        return Category.objects.all()

