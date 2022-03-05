from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)

        # data
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            context = {
                'error': error_message,
                'values': values
            }
            return render(request, 'signup.html', context)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Fisrt Name Required"
        elif len(customer.first_name) < 4:
            error_message = "Firts Name Should be more Than 4 characters"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last Name Should be more Than 4 characters"
        elif not customer.phone:
            error_message = "Phone Number Required"
        elif len(customer.phone) < 4:
            error_message = "Please Enter a valid phone number"
        elif not customer.email:
            error_message = "Email Required"
        elif len(customer.email) < 4:
            error_message = "Please Enter a valid email address"
        elif not customer.password:
            error_message = "Password Required"
        elif customer.isExist():
            error_message = "Email Already Exist!"

        return error_message
