# Generated by Django 3.2.11 on 2022-02-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_auto_20220223_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='subtitle',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
