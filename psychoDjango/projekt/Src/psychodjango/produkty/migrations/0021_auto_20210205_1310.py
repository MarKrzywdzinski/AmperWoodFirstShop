# Generated by Django 3.1.5 on 2021-02-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0020_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='zdjecie',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='i',
            field=models.ImageField(blank=True, upload_to='portfolioImages'),
        ),
    ]