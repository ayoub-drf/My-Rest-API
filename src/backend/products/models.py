from django.db import models
from django.urls import reverse


class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Owner_detail", kwargs={"pk": self.pk})
    

class Product(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
    @property
    def get_sale_price(self):
        return f"{self.price}$"

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"slug": self.slug})

