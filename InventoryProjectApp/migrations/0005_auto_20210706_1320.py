# Generated by Django 3.2.5 on 2021-07-06 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryProjectApp', '0004_auto_20210705_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='landed_till',
        ),
        migrations.RemoveField(
            model_name='product',
            name='landed_to',
        ),
        migrations.RemoveField(
            model_name='product',
            name='technical_data',
        ),
        migrations.RemoveField(
            model_name='product',
            name='used_in',
        ),
    ]
