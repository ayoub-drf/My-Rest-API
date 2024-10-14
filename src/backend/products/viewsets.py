from rest_framework import viewsets, mixins
from products.serializers import ProductSerializer
from products.models import Product
from api.mixins import UserQuerySetMixin

class ProductModelViewSet(UserQuerySetMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user
    #     qs = super().get_queryset(*args, **kwargs)
    #     if not user.is_authenticated:
    #         return Product.objects.none()        
    #     return qs.filter(user=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

        return super().perform_create(serializer)