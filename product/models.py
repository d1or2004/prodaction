from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class PriceTypes(models.TextChoices):
        s = "$", "USD"
        sum = "So'm", "UZS"

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=30, choices=PriceTypes.choices, default=PriceTypes.sum)
    image = models.ImageField(upload_to='products/product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reyting = models.IntegerField()
    kg = models.IntegerField()

    def __str__(self):
        return f"{self.name}  {self.description}"


class ShopDetails(models.Model):
    class PriceTypes(models.TextChoices):
        s = "$", "USD"
        sum = "So'm", "UZS"

    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/shop')
    description = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=30, choices=PriceTypes.choices, default=PriceTypes.sum)


class Savat(Product):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}  {self.description}"

