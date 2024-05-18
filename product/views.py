from django.shortcuts import render

from product.models import Product
from product.book.models import Book
from product.cloth.models import Cloth
from product.mobile.models import Mobile
from store.utils import cartData

# Create your views here.

def product(request, id):
    if request.method == 'GET':
        data = cartData(request)
        cartItems = data['cartItems']
        context = {
            'product': None,
            'book': None,
            'cloth': None,
            'mobile': None,
            'cartItems': cartItems,
            'reviews': None,
            'my_review': None,
        }
        product = Product.objects.get(id=id)
        context['product'] = product

        if product:
            product_object = product.object
            if isinstance(product_object, Book):
                context['book'] = product_object
            elif isinstance(product_object, Cloth):
                context['cloth'] = product_object
            elif isinstance(product_object, Mobile):
                context['mobile'] = product_object

        if request.user.is_authenticated:
            reviews = product.review_set.all().exclude(user=request.user.user_set.get())
            my_review = product.review_set.filter(user=request.user.user_set.get()).first()
        else:
            reviews = product.review_set.all()
            my_review = None

        context['reviews'] = reviews
        context['my_review'] = my_review

        return render(request, 'store/product.html', context)
