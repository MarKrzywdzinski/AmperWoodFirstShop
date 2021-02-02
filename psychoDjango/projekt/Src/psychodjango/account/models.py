
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User, auth
from django.db import models

from produkty.models import Product

# Create your models here.
user = get_user_model()


class Cart(models.Model):

    user = models.ForeignKey(
        user, on_delete=models.CASCADE)
    rzeczyWKoszu = models.ManyToManyField(Product, null=True)
    suma = 0

    def __str__(self):
        return self.user.username
