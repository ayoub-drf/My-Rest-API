from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from random import choice

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


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(name__icontains=query) | Q(slug__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            return self.filter(lookup, user=user)

        return qs
    
class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query=query, user=user)

TAG_MODEL_VALUES = ['cars', 'videos', 'girls', 'boys']

class Product(models.Model):
    user = models.ForeignKey(User, null=True, default=4, on_delete=models.SET_NULL)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    slug = models.SlugField(unique=True)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def is_public(self):
        return self.public

    def get_tag_list(self):
        return [choice(TAG_MODEL_VALUES)]
    
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

