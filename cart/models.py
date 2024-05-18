from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from user.models import User


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)


    def __str__(self):
        return str(self.id)

    @property
    def cart_sub_total(self):
        total = sum([item.get_total for item in self.cartitem_set.all()])
        return total

    @property
    def cart_items_quantity(self):
        quantity = 0
        for item in self.cartitem_set.all():
            quantity = quantity + item.quantity
        return quantity

    @property
    def order_total(self):
        total = self.cart_sub_total
        return total

    class Meta:
        db_table = "carts"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
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
        db_table = "cart_items"
