# Generated by Django 3.1.5 on 2021-01-26 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0008_auto_20210127_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='zdjecie',
            field=models.ImageField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]
