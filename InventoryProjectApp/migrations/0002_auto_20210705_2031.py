# Generated by Django 3.2.5 on 2021-07-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='landed_till',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='prduct_id',
            field=models.IntegerField(),
        ),
    ]
