"""psychodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from strony import views as viewsStrony
from produkty import views as viewsProdukty
from account import views as viewsAccount

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', viewsStrony.home_widok, name='home'),
    path('kontakt/', viewsStrony.kontakt, name='kontakt'),
    path('oNas/', viewsStrony.oNas, name='O nas'),
    path('oWzorach/', viewsStrony.oWzorach, name='O wzorach'),
    path('formularz/', viewsProdukty.produkt_utworz_widok),
    path('Sklep/', viewsProdukty.productsInStore, name='Sklep'),
    path('portfiolio/', viewsProdukty.portfolio, name='Portfolio'),

    re_path(r'^Sklep/(?P<slug>.*)/$', viewsProdukty.SingleProduct,
            name='pojedynczy_produkt'),
    path('accounts/', include('account.urls')),
    re_path(r'^Sklep/(?P<slug>.*)/cart', viewsProdukty.cart, name='cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
