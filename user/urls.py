from django.urls import path

from . import views

urlpatterns = [
    path('logout/', views.do_logout, name="logout"),
    path('login/', views.do_login, name="login"),
    path('register/', views.do_register, name="register"),
    path('me/', views.me, name="me"),
]
