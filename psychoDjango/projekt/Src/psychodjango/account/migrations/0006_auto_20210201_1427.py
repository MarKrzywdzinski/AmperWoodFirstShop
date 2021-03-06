# Generated by Django 3.1.5 on 2021-02-01 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produkty', '0019_auto_20210130_1437'),
        ('account', '0005_auto_20210201_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rzeczyWKoszu', models.ManyToManyField(blank=True, to='produkty.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
