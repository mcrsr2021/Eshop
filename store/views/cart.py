from django.shortcuts import redirect, render
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        context = {
            'products': products
        }
        return render(request, 'cart.html', context)
