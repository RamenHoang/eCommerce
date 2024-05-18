import json

from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import redirect, render

from cart.models import CartItem, Cart
from product.models import Product
from store.utils import cartData, check_authenticate

# Create your views here.
def get_cart(request):
    if not check_authenticate(request):
        return redirect('login')

    data = cartData(request)

    cartItems = data['cartItems']
    cart = data['cart']
    items = data['items']

    context = {'items': items, 'cart': cart, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def add_or_update_cart_item(request):
    if not check_authenticate(request):
        return redirect('login')

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    user = request.user.user_set.get()
    product = Product.objects.get(id=productId)
    product_object = product.object
    cart, created = Cart.objects.get_or_create(user=user)

    cartItem, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type_id=ContentType.objects.get_for_model(product_object).id,
        object_id=product.id
    )

    message = ''
    if action == 'add':
        cartItem.quantity = (cartItem.quantity + 1)
        message = f'Added 1 item <strong>"{product.name}"</strong> to cart'
    elif action == 'remove':
        cartItem.quantity = (cartItem.quantity - 1)
        message = f'Removed 1 item <strong>"{product.name}"</strong> from cart'

    cartItem.save()

    if cartItem.quantity <= 0:
        cartItem.delete()

    alert_html_response = render(request, 'store/alert-success.html', {
        'alert': {
            'message': message,
        }
    })

    return JsonResponse(
        {
            'alert_block': alert_html_response.content.decode('utf-8'),
            'cart_total': cart.cart_items_quantity,
        }
    )