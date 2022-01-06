from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import Product
from .models import Category
from .models import Customer
from.forms import Customer_form, Login_form
from django.contrib import messages


def index(request):
    product=Product.objects.all()
    category=Category.get_all_category()
    param={'product':product,'category':category}
    return render(request,'index.html',param)


def sign_up(request):
    if request.method == 'POST':
        print("post mehod running")
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
        print('Get method is running ')
    data={'form':customer, }
    return render(request,'sign_up.html',data)


def log_in(request):
    form=Login_form()
    print(form)
    param={'form':form}
    return render(request,'login.html',param)
