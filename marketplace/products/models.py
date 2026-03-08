from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=200)
    origin = models.CharField(max_length=100)
    roast = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
