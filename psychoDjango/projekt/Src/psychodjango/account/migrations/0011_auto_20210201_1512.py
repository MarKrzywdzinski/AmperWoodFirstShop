# Generated by Django 3.1.5 on 2021-02-01 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0019_auto_20210130_1437'),
        ('account', '0010_remove_cart_rzeczywkoszu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='ItemsInCart',
        ),
    ]
