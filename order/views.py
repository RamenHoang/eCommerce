import datetime
from django.shortcuts import redirect, render

from order.models import Order, OrderItem
from order.utils import complete_order
from payment.models import Payment
from store.utils import cartData, check_authenticate, check_payment_information

errors = {}


# Create your views here.
def checkout(request):
    if not check_authenticate(request):
        return redirect('login')

    cart_data = cartData(request)
    if cart_data['cartItems'] == 0:
        return redirect('store')

    if request.method == 'GET':
        request_data = request.GET.dict()
        cartItems = cart_data['cartItems']
        cart = cart_data['cart']
        items = cart_data['items']

        order, created = Order.objects.get_or_create(
            user=request.user.user_set.get(), complete=False)

        if order.shipment is None:
            return redirect('shipment')

        payments = Payment.objects.all()

        selected_payment = payments[0]
        if request_data.get('payment_id'):
            selected_payment = payments.get(id=request_data.get('payment_id'))

        alerts = []
        if errors.get(request.user.user_set.get().id):
            for error in errors[request.user.user_set.get().id]:
                alerts.append({
                    'message': error,
                    'type': 'error'
                })

            errors[request.user.user_set.get().id] = []

        context = {
            'items': items,
            'cart': cart,
            'cartItems': cartItems,
            'order': order,
            'payments': payments,
            'selected_payment': selected_payment,
            'user': request.user.user_set.get(),
            'alerts': alerts
        }
        return render(request, 'store/checkout.html', context)
    elif request.method == 'POST':
        transaction_id = datetime.datetime.now().timestamp()
        user = request.user.user_set.get()
        order, created = Order.objects.get_or_create(user=user, complete=False)
        order.transaction_id = transaction_id
        payment = Payment.objects.get(id=request.POST['payment_id'])

        if check_payment_information(payment.type, request.POST.dict()):
            order.payment = payment
        else:
            if errors.get(user.id):
                errors[user.id].append('Payment information is not valid')
            else:
                errors[user.id] = ['Payment information is not valid']

            return redirect('checkout')

        cart = cart_data['cart']
        items = cart_data['items']

        for item in items:
            OrderItem.objects.create(
                order=order,
                object_id=item.object_id,
                quantity=item.quantity,
                content_type_id=item.content_type_id
            )

        for item in items:
            item.delete()
        cart.delete()

        complete_order(order, user)

        return redirect('order_detail', id=order.id)


def order_detail(request, id):
    if not check_authenticate(request):
        return redirect('login')

    cart_data = cartData(request)
    cartItems = cart_data['cartItems']
    if request.method == 'GET':
        order = Order.objects.get(id=id)

        context = {
            'order': order,
            'user': request.user.user_set.get(),
            'cartItems': cartItems,
        }
        return render(request, 'store/order_detail.html', context)


def orders(request):
    if not check_authenticate(request):
        return redirect('login')

    cart_data = cartData(request)
    cartItems = cart_data['cartItems']
    user = request.user.user_set.get()
    orders = Order.objects.filter(user=user, complete=True).order_by('-id')

    context = {
        'orders': orders,
        'cartItems': cartItems,
    }
    return render(request, 'store/orders.html', context)
