from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('orders', views.orders, name="orders"),
    path('order_detail/<int:id>', views.order_detail, name="order_detail"),
]
