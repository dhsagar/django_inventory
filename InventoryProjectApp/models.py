from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    prduct_id = models.IntegerField()
    purchase_date = models.CharField(max_length=100)
    owner = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    used_in = models.CharField(max_length=200, null=True, default='')
    technical_data = models.TextField(null=True, default='')
    landed_to = models.CharField(max_length=200, blank=True, null=True)
    landed_till = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
