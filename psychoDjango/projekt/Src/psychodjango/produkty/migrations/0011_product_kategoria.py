# Generated by Django 3.1.5 on 2021-01-29 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0010_remove_product_kategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kategoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produkty.kategoria'),
            preserve_default=False,
        ),
    ]