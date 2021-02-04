from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages

from account.models import Cart
from produkty.models import Product
from produkty.views import SingleProduct

# Create your views here.


def login(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Zle dane')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request, *args, **kwargs):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
                messages.info(request, 'Nazwa użytkownika już istnieje')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email zajety')
                messages.info(request, 'Email już istnieje')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('password nie pasuje')
            messages.info(request, 'Hasla nie pasują')
            return redirect('register')
        return redirect('home')
    else:
        return render(request, 'register.html', {})


