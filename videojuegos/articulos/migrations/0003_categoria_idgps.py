# Generated by Django 4.0.2 on 2024-06-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_categoria_alter_articulos_stock_articulos_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='idgps',
            field=models.CharField(default='NONE', max_length=100),
            preserve_default=False,
        ),
    ]
