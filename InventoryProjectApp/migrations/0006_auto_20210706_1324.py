# Generated by Django 3.2.5 on 2021-07-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryProjectApp', '0005_auto_20210706_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='landed_till',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='landed_to',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='technical_data',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='used_in',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]