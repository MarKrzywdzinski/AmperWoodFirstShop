# Generated by Django 3.1.5 on 2021-02-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0019_auto_20210130_1437'),
        ('account', '0011_auto_20210201_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='rzeczyWKoszu',
            field=models.ManyToManyField(to='produkty.Product'),
        ),
        migrations.DeleteModel(
            name='ItemsInCart',
        ),
    ]
