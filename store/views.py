from django.shortcuts import render
from product.models import Product
from .utils import cartData


def store(request):
    data = cartData(request)

    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)
