# Generated by Django 3.2.11 on 2022-02-17 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_remove_noticiasindexpage_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticiaspage',
            name='portada',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
