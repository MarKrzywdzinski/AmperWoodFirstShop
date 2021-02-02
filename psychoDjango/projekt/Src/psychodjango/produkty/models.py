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
