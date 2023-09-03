from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    # preview = models...
    category = models.CharField(max_length=50)
    retail_price = models.IntegerField(default = 0)
    date_initial = models.DateTimeField
    date_changes = models.DateTimeField



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
