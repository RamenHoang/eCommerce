from cart.models import Cart


def cartData(request):
    cartItems = None
    cart = None
    items = None

    if request.user.is_authenticated:
        user = request.user.user_set.get()
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartitem_set.all()
        cartItems = cart.cart_items_quantity

    return {
        'cartItems': cartItems,
        'cart': cart,
        'items': items
    }


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
            if (
                data['card_number'] == card['card_number']
                and data['name_on_card'] == card['name_on_card']
                and data['expiry_date'] == card['expiry_date']
                and data['security_code'] == card['security_code']
            ):
                return True
    elif payment_type == 'cod':
        return True

    return False
