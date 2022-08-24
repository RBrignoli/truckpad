# Generated by Django 4.1 on 2022-08-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_driverreport_has_cargo_to_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='latitude',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Coordenadas Geográficas (lat)'),
        ),
        migrations.AddField(
            model_name='address',
            name='longitude',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Coordenadas Geográficas (long)'),
        ),
        migrations.AddField(
            model_name='driverprofile',
            name='gender',
            field=models.CharField(choices=[('man', 'Homen'), ('woman', 'Mulher'), ('transgender', 'Transgenero'), ('non_binary', 'Não binário'), ('prefer_not_to_respond', 'Prefere não responder')], default='prefer_not_to_respond', max_length=32, verbose_name='Gênero'),
        ),
    ]
