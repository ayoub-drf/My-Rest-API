from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from products.models import Product




def validate_name(value):
    qs = Product.objects.filter(name__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"this name ({value}) already in use")
    return value


def unique_name(value):
    return UniqueValidator(Product.objects.all(), lookup='exact')