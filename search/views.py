from django.shortcuts import render

from product.models import Product
from store.utils import cartData

# Create your views here.


def search(request):
    if request.method == 'GET':
        request_data = request.GET.dict()

        data = cartData(request)
        cartItems = data['cartItems']

        products = Product.objects.filter(
            name__icontains=request_data.get('q'))
        context = {'products': products, 'cartItems': cartItems}
        return render(request, 'store/store.html', context)
