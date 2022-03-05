from django.shortcuts import redirect, render
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Orders
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class OrdersView(View):

    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Orders.get_orders_by_customer_id(customer)
        context = {
            'orders': orders
        }
        return render(request, 'orders.html', context)
