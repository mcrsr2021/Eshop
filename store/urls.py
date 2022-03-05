from unicodedata import name
from django.urls import path
from store.views import index, login, signup, logout, cart, checkout, ordersview

urlpatterns = [
    path('', index.Index.as_view(), name="index"),
    path('signup/', signup.Signup.as_view(), name="signup"),
    path('login/', login.Login.as_view(), name="login"),
    path('logout/', logout.Logout.as_view(), name="logout"),
    path('cart/', cart.Cart.as_view(), name="cart"),
    path('checkout/', checkout.Checkout.as_view(), name="checkout"),
    path('orders/', ordersview.OrdersView.as_view(), name="orders"),
]
