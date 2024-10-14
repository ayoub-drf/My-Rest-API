from django.db import models
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

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
    user = models.ForeignKey(User, null=True, default=4, on_delete=models.SET_NULL)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def discount(self):
        return f"{self.price}$"

    def __str__(self):
        return self.name
    
    @property
    def get_sale_price(self):
        return f"{self.price}$"

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"slug": self.slug})

