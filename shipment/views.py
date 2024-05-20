from django.shortcuts import redirect, render

from order.models import Order
from shipment.models import Shipment
from store.utils import cartData, check_authenticate

# Create your views here.


def shipment(request):
    if not check_authenticate(request):
        return redirect('login')

    cart_data = cartData(request)

    if cart_data['cartItems'] == 0:
        return redirect('store')

    user = request.user.user_set.get()
    order, created = Order.objects.get_or_create(user=user, complete=False)

    if request.method == 'GET':

        shipments = Shipment.objects.all()
        selected_shipment = shipments[0]
        if order.shipment is not None:
            selected_shipment = order.shipment

        context = {
            'shipments': shipments,
            'selected_shipment': selected_shipment,
            'cartItems': cart_data['cartItems'],
        }
        return render(request, 'store/shipment.html', context)
    elif request.method == 'POST':
        request_data = request.POST.dict()
        order.shipment = Shipment.objects.get(
            id=request_data.get('shipment_id'))
        order.save()

        return redirect('checkout')
