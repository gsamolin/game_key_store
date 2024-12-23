from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Unique name for the category
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)  # Product name
    description = models.TextField()  # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    quantity = models.PositiveIntegerField()  # Available quantity in stock
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Category the product belongs to

    def __str__(self):
        return self.name