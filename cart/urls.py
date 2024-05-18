from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.get_cart, name="cart"),
    path('update_item/', views.add_or_update_cart_item, name="update_item"),
]