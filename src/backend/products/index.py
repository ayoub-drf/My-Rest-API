from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex

from products.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'name',
        'public',
        'user',
    ]
    tags = 'get_tag_list'