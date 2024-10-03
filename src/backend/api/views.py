from django.forms.models import model_to_dict
from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_home(request):
    product = Product.objects.all().order_by('?').first()

    data = model_to_dict(product, fields=('id', 'name', 'price',))

    return Response(data=data)