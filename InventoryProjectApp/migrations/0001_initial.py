# Generated by Django 3.2.5 on 2021-07-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('prduct_id', models.IntegerField(max_length=100)),
                ('purchase_date', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('used_in', models.CharField(max_length=200)),
                ('technical_data', models.TextField()),
                ('landed_to', models.CharField(max_length=200)),
                ('landed_till', models.CharField(max_length=200)),
            ],
        ),
    ]
