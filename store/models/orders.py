from django.db import models
from django.utils import timezone
from store.models.product import Product
from store.models.customer import Customer


class Orders(models.Model):
    ORDER_STATUS = [
        ('PENDING', 'Pending'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=15)
    status = models.CharField(choices=ORDER_STATUS,
                              max_length=10, default='Pending')

    def placeorder(self):
        return self.save()

    @staticmethod
    def get_orders_by_customer_id(customer_id):
        return Orders.objects.filter(customer=customer_id)
