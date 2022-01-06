from django import forms
from django.forms import fields
from .models import  Customer

class Customer_form(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        labels={'f_name':'First Name',
                'l_name':'Last Name',
                'email':'Email Address',
                're_password':'Reenter Password' }

        widgets={'f_name':forms.TextInput(attrs={'class':'somecss','id':'fname'}),
                'l_name':forms.TextInput(attrs={'class':'somecss','id':'lname'}),
                'email':forms.EmailInput(attrs={'class':'somecss','id':'email',
                'placeholder':'abc@gmail.com'}),
                'password':forms.PasswordInput(attrs={'class':'somecss',
                'id':'password','placeholder':'*****'}),
                're_password':forms.PasswordInput(attrs={'class':'somecss',
                'id':'repassword','placeholder':'*****'}),
                
}


class Login_form(forms.ModelForm):
        class Meta:
                model=Customer
                fields=['f_name','email','password','re_password']