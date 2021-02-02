from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from strony import views as viewsStrony
from produkty import views as viewsProdukty
from account import views as viewsAccount


urlpatterns = [
    path('register', viewsAccount.register, name='register'),
    path('login', viewsAccount.login, name='login'),
    path('logout', viewsAccount.logout, name='logut')
]
