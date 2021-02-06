from django.db import models

# Create your models here.


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.nazwa


class Product(models.Model):
    nazwa = models.CharField(max_length=120)
    opis = models.TextField()
    cena = models.FloatField()
    zdjecie = models.ImageField(height_field=None, upload_to='fotki')
    podsumowanie = models.TextField(
        default="Django jest spoko")

    przecena = models.BooleanField(default=False)
    kategoria = models.ForeignKey(
        Kategoria, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        unique_together = ('nazwa', 'slug')

    def __str__(self):
        return self.nazwa


class Portfolio(models.Model):
    P = []

    title = models.CharField(max_length=70)

    photo1 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo2 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo3 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo4 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo5 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo6 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo7 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo8 = models.ImageField(upload_to='portfolioImages', blank=True)
    photo9 = models.ImageField(upload_to='portfolioImages', blank=True)

    P.append(photo1)
    P.append(photo2)
    P.append(photo3)
    P.append(photo4)
    P.append(photo5)
    P.append(photo6)
    P.append(photo7)
    P.append(photo8)
    P.append(photo9)

    def __str__(self):
        return self.title
