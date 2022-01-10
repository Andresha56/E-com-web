from django import forms
from django.forms import fields
from .models import  Customer

# ----------code for sign_up page-------------

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

#      ----------code for log_in page----------------


class Login_form(forms.ModelForm):
        class Meta:
                model=Customer
                fields=['f_name','password']

                labels={'f_name':'User name',
                'email':'Email',
                're_password':'Reenter Password' }


                widgets={
                        'f_name':forms.TextInput(attrs={'class':'css','id':'f_name'}),
                        'email':forms.EmailInput(attrs={'class':'css','id':'email'}),
                         'password':forms.PasswordInput(attrs={'class':'css',
                        'id':'password','placeholder':'*****'}),
                      
                
                }