# Generated by Django 3.2.5 on 2021-07-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryProjectApp', '0002_auto_20210705_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='landed_till',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='landed_to',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
