import algoliasearch_django as algoliasearch

from products.models import Product

algoliasearch.register(Product)