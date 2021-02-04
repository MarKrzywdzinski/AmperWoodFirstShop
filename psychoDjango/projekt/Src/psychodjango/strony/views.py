from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from produkty.models import Product


def home_widok(request, *args, **kwargs):
    return render(request, "index.html", {})


def kontakt(request, *args, **kwargs):
    return render(request, "home.html", {})


def oNas(request, *args, **kwargs):
    kontekst = {
        "moje_dane": "krzywdziński Marcin",
        "numer_telefonu": 123
    }
    return render(request, "onas.html", kontekst)

def oWzorach(request, *args, **kwargs):
    return render(request, "wzory.html", {})

