from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponseRedirect
from django.views import View

from .models import Product
from .models import Category
from .models import Customer
from.forms import Customer_form, Login_form 
from django.contrib import messages


def index(request):
    product=Product.objects.all()
    category=Category.get_all_category()
    product_category=(request.GET.get(' product category'))
    if product_category:
        product= Product.get_product_by_product_category_id(product_category)  
    else:
        product=Product.objects.all()
    param={'product':product,'category':category}
    return render(request,'index.html',param)






#  ---------sign_up_page---------
def sign_up(request):
    if request.method == 'POST':
        customer=Customer_form(request.POST)
        if customer.is_valid():
            f_name=(customer.cleaned_data['f_name'])
            l_name=(customer.cleaned_data['l_name'])
            email=(customer.cleaned_data['email'])
            password=(customer.cleaned_data['password'])
            re_password=(customer.cleaned_data['re_password'])

            if password != re_password:
                messages.add_message(request,messages.ERROR,'Password does not match !!')

            elif len(password and re_password) <8:
                messages.add_message(request,messages.ERROR,'Password must be 7 digit long or more !!')
            else:
                register=Customer(f_name=f_name,
                                    l_name=l_name,
                                    email=email,
                                    password=password,
                                    re_password=re_password
                                    )
                register.save()
                return redirect('homepage')

    else:
        customer=Customer_form()
    data={'form':customer, }
    return render(request,'sign_up.html',data)


# ------------Log_in_page------------

def log_in(request):
    if request.method=='POST':
        log_in=Login_form(request.POST)
        if log_in.is_valid():
            user_name=log_in.cleaned_data['f_name']
            password=log_in.cleaned_data['password']
            try:
                customer=Customer.get_customer_by_username(f_name=user_name)
            except Exception as a:
                messages.add_message(request,messages.ERROR,'User name or password is invalid ')
                return redirect('log_in_page')
            if  customer:
                print(customer.password)
                if password==customer.password:
                    return redirect('homepage')
                else:
                    messages.add_message(request,messages.ERROR,'User name or password is invalid ')                    
    else: 
        log_in=Login_form()

    param={'log_in_form':log_in}
    return render(request,'login.html',param)
