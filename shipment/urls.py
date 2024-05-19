from django.urls import path
from . import views

urlpatterns = [
    path('shipment/', views.shipment, name="shipment"),
]
