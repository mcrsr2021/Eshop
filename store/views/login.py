from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    next = None

    def get(self, request):
        Login.next = request.GET.get('next')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                if Login.next:
                    return HttpResponseRedirect(Login.next)
                else:
                    Login.next = None
                    return redirect('index')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"
        return render(request, 'login.html', {'error': error_message})
