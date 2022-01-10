
from django.db import models


class Customer(models.Model):
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    re_password=models.CharField(max_length=8)


    def email_exist(self):
        if Customer.objects.filter(email=self.email):
           return True
        else:
            return False

    @staticmethod
    def get_customer_by_username(f_name):
        return Customer.objects.get(f_name=f_name)