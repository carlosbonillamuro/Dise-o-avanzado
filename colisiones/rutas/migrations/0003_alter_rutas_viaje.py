# Generated by Django 4.0.2 on 2024-06-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0002_rutas_viaje_alter_personal_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutas',
            name='viaje',
            field=models.IntegerField(verbose_name='No de viaje'),
        ),
    ]
