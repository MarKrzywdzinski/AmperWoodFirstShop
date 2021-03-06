from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, auth
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
# Create your views here.
from produkty.models import Product
from .forms import ProductForm
from account.models import Cart
from produkty.models import Portfolio

itemyWKoszyku = []
user = get_user_model()


def produkt_utworz_widok(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, "produkty_utworz.html", context)


def produkt_opis_widok(request):
    obj = Product
    kontekst = {
        'nazwa': obj.nazwa,
        'opis': obj.opis
    }
    return render(request, "opis.html", kontekst)


def productsInStore(request):

    obj = Product.objects.all()

    return render(request, 'Sklep.html', {'obj': obj})


def SingleProduct(request, slug):
    print(slug)
    obj_slug = get_object_or_404(Product, slug=slug)
    obj = Product.objects.get(slug=slug)

    if request.method == 'POST':
        koszyk = Cart.objects.get()
        item = koszyk.rzeczyWKoszu.get(slug=slug)
        itemyWKoszyku.append(item)
        print('Added SigleProduct to cart', user, koszyk, item,
              item.slug, itemyWKoszyku)
        kontext = {
            'produkt404_slug': obj_slug,
            'obj': obj,
            'koszyk': koszyk,
            'item': item,
            'slugi': item.slug,
            'itemyWKoszyku': itemyWKoszyku
        }

    else:
        kontext = {
            'produkt404_slug': obj_slug,
            'obj': obj,
        }

    return render(request, 'produkt.html', kontext)


def cart(request, slug):
    suma = 0
    for i in itemyWKoszyku:
        suma = suma + i.cena
        print(suma)

    return render(request, 'cart.html', {'itemyWKoszyku': itemyWKoszyku, 'suma': suma})


def portfolio(request, *args, **kwargs):
    porto = []
    p = Portfolio.objects.all()
    p = p.first()

    porto.append(p.photo1)
    porto.append(p.photo2)
    porto.append(p.photo3)
    porto.append(p.photo4)
    porto.append(p.photo5)
    porto.append(p.photo6)
    porto.append(p.photo7)
    porto.append(p.photo8)
    porto.append(p.photo9)
    kontekst = {
        "porto": porto
    }

    return render(request, "portfolio.html", kontekst)
