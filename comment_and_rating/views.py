from django.shortcuts import render, redirect

from comment_and_rating.models import Review
from product.models import Product
from store.utils import check_authenticate


# Create your views here.

def review(request):
    if not check_authenticate(request):
        return redirect('login')

    if request.method == 'POST':
        data = request.POST.dict()
        product = Product.objects.get(id=data.get('product_id'))
        user = request.user.user_set.get()
        rating = data.get('rating')
        comment = data.get('comment')

        review, created = Review.objects.get_or_create(product=product, user=user)
        review.rating = rating
        review.comment = comment
        review.save()

        return redirect('product', id=product.id)
