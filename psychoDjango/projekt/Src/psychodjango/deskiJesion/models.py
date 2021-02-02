from django.db import models

# Create your models here.


class deskaJesion(models.Model):
    nazwa = models.CharField(max_length=120)
    zdjecie = models.ImageField()
    opis = models.TextField()
    cena = models.FloatField()
    podsumowanie = models.TextField(default="Django jest spoko")
    przecena = models.BooleanField(default=False)
