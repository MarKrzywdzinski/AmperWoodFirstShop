# Generated by Django 3.1.5 on 2021-02-01 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='rzeczyWKoszu',
        ),
    ]
