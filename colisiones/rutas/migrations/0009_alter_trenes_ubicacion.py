# Generated by Django 4.0.2 on 2024-06-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0008_alter_rutas_viajes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trenes',
            name='ubicacion',
            field=models.CharField(max_length=22, verbose_name='Ubicación'),
        ),
    ]