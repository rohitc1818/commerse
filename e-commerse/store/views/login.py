from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
# password hashing module#
from django.contrib.auth.hashers import check_password


def logout(request):
    request.session.clear()
    return redirect('login')



class Login(View):
    return_url = None
    def get(self,request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        value = {
            'email':email,
            'password':password
        }
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('homepage')
            else:
                error_message = 'Email or password is invalid!!!'
        else:
            error_message = 'Email and password is invalid!!!'

        data = {
            'error':error_message,
            'values':value
        }

        print(email, password)
        print('you are ', email)
        return render(request, 'login.html', data)


