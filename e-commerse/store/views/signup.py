from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
# password hashing module#
from django.contrib.auth.hashers import make_password



class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        First_name = postData.get('firstname')
        Last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # dictionary for signup age
        value = {
            'First_name': First_name,
            'Last_name': Last_name,
            'phone': phone,
            'email': email
        }
        # customer objects.
        customer = Customer(First_name=First_name,
                            Last_name=Last_name,
                            phone=phone,
                            email=email,
                            password=password)

        # reformat code #
        error_message = self.Validatecustomer(customer)
        # reformat code #

        # data saving
        if not error_message:
            print(First_name, Last_name, phone, email, password)
            # password hashing #

            customer.password = make_password(customer.password)

            # password hashing #
            customer.Register()
            return redirect('homepage')
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'signup.html', data)

    def Validatecustomer(self,customer):
        # form validations.
        error_message = None
        if not customer.First_name:
            error_message = "First_name required"
        elif len(customer.First_name) < 3:
            error_message = "First name must be 3 character long or more"
        elif not customer.Last_name:
            error_message = "Last_name required"
        elif len(customer.Last_name) < 4:
            error_message = "Last name must be 4 character long or more "
        elif not customer.phone:
            error_message = "Phone number required"
        elif len(customer.phone) < 10:
            error_message = 'Phone number must be 10 character'
        elif len(customer.email) < 6:
            error_message = 'Email must be 5 character long'
        elif not customer.password:
            error_message = "create your password to register "
        elif len(customer.password) < 6:
            error_message = 'password must be 6 character long'
        elif customer.isExists():
            error_message = "Email already register"
        return error_message