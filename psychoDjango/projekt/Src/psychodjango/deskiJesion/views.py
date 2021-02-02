from django.shortcuts import render

# Create your views here.
from .models import deskaJesion


def pokazDeskaJesion(request, *args, **kwargs):
    obj = deskaJesion.objects.get(id=1)
    kontekst = {
        'nazwa': obj.nazwa,
        'opis': obj.opis,
        'zdjecie': obj.zdjecie,
        'cena': obj.cena,
        'przecena': obj.przecena,
        'ilosc': obj.ilosc
    }
    return render(request, "Sklep.html", kontekst)
