# Generated by Django 3.2.11 on 2022-01-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
