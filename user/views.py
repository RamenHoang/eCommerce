from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser

from store.utils import check_authenticate, cartData
from user.models import Address, Fullname, User

# Create your views here.


def do_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return render(request, 'store/login.html')
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        auth_user = authenticate(request, username=username, password=password)
        if auth_user is not None:
            if auth_user.user_set.count() == 0:
                User.objects.create(account=auth_user)

            login(request, auth_user)
            return redirect('store')
        else:
            return redirect('login')


def do_register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return render(request, 'store/register.html')
    elif request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        no_house = request.POST["no_house"]
        street = request.POST["street"]
        city = request.POST["city"]
        state = request.POST["state"]
        zipcode = request.POST["zipcode"]

        auth_user = AuthUser.objects.create_user(username, email, password)
        auth_user.save()

        address = Address.objects.create(
            no_house=no_house, street=street, city=city, state=state, zipcode=zipcode)
        address.save()

        fullname = Fullname.objects.create(
            firstname=firstname, lastname=lastname)
        fullname.save()

        user = User.objects.create(
            account=auth_user, fullname=fullname, address=address)
        user.save()

        return redirect('login')


def do_logout(request):
    logout(request)
    return redirect('login')


def me(request):
    if not check_authenticate(request):
        return redirect('login')

    data = cartData(request)
    cartItems = data['cartItems']

    if request.method == 'GET':
        user = request.user.user_set.get()

        context = {
            'user': user,
            'cartItems': cartItems,
        }
        return render(request, 'store/me.html', context)
    elif request.method == 'POST':
        request_data = request.POST.dict()

        # Update auth user
        request.user.username = request_data.get('username')
        if request_data.get('password'):
            request.user.set_password(request_data.get('password'))
        request.user.email = request_data.get('email')
        request.user.save()

        user = request.user.user_set.get()

        if user.fullname is None:
            # Create fullname
            user.fullname = Fullname.objects.create(
                firstname=request_data.get('firstname'),
                lastname=request_data.get('lastname')
            )
            user.save()
        else:
            # Update fullname
            user.fullname.firstname = request_data.get('firstname')
            user.fullname.lastname = request_data.get('lastname')
            user.fullname.save()

        if user.address is None:
            # Create address
            user.address = Address.objects.create(
                no_house=request_data.get('no_house'),
                street=request_data.get('street'),
                city=request_data.get('city'),
                state=request_data.get('state'),
                zipcode=request_data.get('zipcode')
            )
            user.save()
        else:
            # Update address
            user.address.no_house = request_data.get('no_house')
            user.address.street = request_data.get('street')
            user.address.city = request_data.get('city')
            user.address.state = request_data.get('state')
            user.address.zipcode = request_data.get('zipcode')
            user.address.save()

        return redirect('me')
