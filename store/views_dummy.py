# from django.shortcuts import redirect, render
# from django.contrib.auth.hashers import make_password, check_password
# from store.models.customer import Customer
# from store.models.product import Product
# from store.models.category import Category
# from django.views import View


# def index(request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryId = request.GET.get('category')
#     if categoryId:
#         products = Product.get_all_products_by_id(categoryId)
#     else:
#         products = Product.get_all_products()
#     context = {
#         'products': products,
#         'categories': categories
#     }
#     return render(request, 'index.html', context)


# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         postData = request.POST
#         first_name = postData.get('first_name')
#         last_name = postData.get('last_name')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')

#         customer = Customer(first_name=first_name, last_name=last_name,
#                             phone=phone, email=email, password=password)

#         # data
#         values = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone': phone,
#             'email': email
#         }

#         # validation
#         error_message = None
#         if not first_name:
#             error_message = "Fisrt Name Required"
#         elif len(first_name) < 4:
#             error_message = "Firts Name Should be more Than 4 characters"
#         elif not last_name:
#             error_message = "Last Name Required"
#         elif len(last_name) < 4:
#             error_message = "Last Name Should be more Than 4 characters"
#         elif not phone:
#             error_message = "Phone Number Required"
#         elif len(phone) < 4:
#             error_message = "Please Enter a valid phone number"
#         elif not email:
#             error_message = "Email Required"
#         elif len(email) < 4:
#             error_message = "Please Enter a valid email address"
#         elif not password:
#             error_message = "Password Required"
#         elif customer.isExist():
#             error_message = "Email Already Exist!"

#         if not error_message:
#             customer.password = make_password(customer.password)
#             customer.register()
#             return redirect('index')
#         else:
#             context = {
#                 'error': error_message,
#                 'values': values
#             }
#             return render(request, 'signup.html', context)


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         error_message = None
#         customer = Customer.get_customer_by_email(email)
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('index')
#             else:
#                 error_message = "Email or Password Invalid"
#         else:
#             error_message = "Email or Password Invalid"
#         return render(request, 'login.html', {'error': error_message})
