from django.utils.timezone import now

from order.models import Order
from user.models import User


def complete_order(order: Order, user: User):
    order.complete = True
    order.date_order = now()
    order.total = order.order_total
    order.subtotal = order.order_sub_total
    order.shipping_cost = order.order_shipping_cost
    order.address = user.address
    order.save()
