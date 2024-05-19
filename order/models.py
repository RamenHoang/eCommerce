from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.timezone import now

from user.models import User, Address
from payment.models import Payment
from shipment.models import Shipment


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(
        Payment, on_delete=models.SET_NULL, null=True, blank=True)
    shipment = models.ForeignKey(
        Shipment, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)

    @property
    def order_sub_total(self):
        total = sum([item.get_total for item in self.orderitem_set.all()])
        return total

    @property
    def order_items_quantity(self):
        quantity = 0
        for item in self.orderitem_set.all():
            quantity = quantity + item.quantity
        return quantity

    @property
    def order_shipping_cost(self):
        shipping_cost = self.shipment.cost
        return shipping_cost

    @property
    def order_total(self):
        total = self.order_sub_total + self.order_shipping_cost
        return total

    class Meta:
        db_table = "orders"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.content_object.price * self.quantity
        return total

    class Meta:
        db_table = "order_items"
