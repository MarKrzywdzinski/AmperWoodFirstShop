# Generated by Django 3.1.5 on 2021-01-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deskaJesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=120)),
                ('zdjecie', models.ImageField(upload_to='')),
                ('opis', models.TextField()),
                ('cena', models.FloatField()),
                ('podsumowanie', models.TextField(default='Django jest spoko')),
                ('przecena', models.BooleanField(default=False)),
            ],
        ),
    ]
