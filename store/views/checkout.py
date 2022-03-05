from django.shortcuts import redirect
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Orders


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customr = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Orders(
                product=product,
                customer=Customer(id=customr),
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address,
                phone=phone
            )
            order.placeorder()
        request.session['cart'] = {}
        return redirect('index')
