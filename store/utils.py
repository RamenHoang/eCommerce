import json

from django.shortcuts import redirect

from cart.models import Cart
from order.models import Order, OrderItem
from product.models import Product
from user.models import User


# def cookieCart(request):
#     # Create empty cart for now for non-logged in user
#     try:
#         cart = json.loads(request.COOKIES['cart'])
#     except:
#         cart = {}
#         print('CART:', cart)

#     items = []
#     order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
#     cartItems = order['get_cart_items']

#     for i in cart:
#         # We use try block to prevent items in cart that may have been removed from causing error
#         try:
#             if (cart[i]['quantity'] > 0):  # items with negative quantity = lot of freebies
#                 cartItems += cart[i]['quantity']

#                 product = Product.objects.get(id=i)
#                 total = (product.price * cart[i]['quantity'])

#                 order['get_cart_total'] += total
#                 order['get_cart_items'] += cart[i]['quantity']

#                 item = {
#                     'id': product.id,
#                     'product': {'id': product.id, 'name': product.name, 'price': product.price,
#                                 'imageURL': product.imageURL}, 'quantity': cart[i]['quantity'],
#                     'digital': product.digital, 'get_total': total,
#                 }
#                 items.append(item)

#                 if product.digital == False:
#                     order['shipping'] = True
#         except:
#             pass

#     return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    cartItems = None
    cart = None
    items = None

    if request.user.is_authenticated:
        user = request.user.user_set.get()
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartitem_set.all()
        cartItems = cart.cart_items_quantity
    # if request.user.is_authenticated:
    #     user = request.user.user_set.get()
    #     cart, created = Cart.objects.get_or_create(user=user)
    #     items = cart.cartitem_set.all()
    #     cartItems = cart.cart_items_quantity
    # else:
    #     cookieData = cookieCart(request)
    #     cartItems = cookieData['cartItems']
    #     order = cookieData['order']
    #     items = cookieData['items']

    return {
        'cartItems': cartItems,
        'cart': cart,
        'items': items
    }


# def guestOrder(request, data):
#     name = data['form']['name']
#     email = data['form']['email']

#     cookieData = cookieCart(request)
#     items = cookieData['items']

#     customer, created = User.objects.get_or_create(
#         email=email,
#     )
#     customer.name = name
#     customer.save()

#     order = Order.objects.create(
#         customer=customer,
#         complete=False,
#     )

#     for item in items:
#         product = Product.objects.get(id=item['id'])
#         OrderItem.objects.create(
#             product=product,
#             order=order,
#             quantity=(item['quantity'] if item['quantity'] > 0 else -1 * item['quantity']),
#             # negative quantity = freebies
#         )
#     return customer, order


def check_authenticate(request):
    if not request.user or not request.user.is_authenticated:
        return False
    return True


def get_available_cards():
    return [
        {
            "card_number": "4242424242424242",
            "name_on_card": "TEST TEST TEST",
            "expiry_date": "12/30",
            "security_code": "123"
        }
    ]


def check_payment_information(payment_type, data):
    if payment_type == 'card':
        cards = get_available_cards()
        for card in cards:
            if (data['card_number'] == card['card_number']
                    and data['name_on_card'] == card['name_on_card']
                    and data['expiry_date'] == card['expiry_date']
                    and data['security_code'] == card['security_code']):
                return True
    elif payment_type == 'cod':
        return True

    return False
