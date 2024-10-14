from products.models import Owner, Product
from products.serializers import ProductSerializer, OwnerSerializer
from rest_framework.generics import RetrieveAPIView, CreateAPIView

from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
)

from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication

from .permissions import IsStaffEditorPermissions

from .authentication import token_auth_base
from .mixins import StaffEditorPermissionsMixin

class ProductMixinAPIView(
                        StaffEditorPermissionsMixin,
                        mixins.ListModelMixin, generics.GenericAPIView,
                        mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    









# Products
class ProductDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'product_slug'

product_detail_view = ProductDetailRetrieveAPIView.as_view()


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')
        # name = serializer.validated_data.get('name') or None
        serializer.save()

product_create_view = ProductCreateAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def product_list_create_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        if pk is not None:
            queryset = get_object_or_404(Product, id=pk)
            serializer = ProductSerializer(queryset).data
            return Response(data=serializer, status=status.HTTP_200_OK)
        
    if method == 'POST':
        product = request.data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name', None)
            if name:
                serializer.save(name=name.upper())

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)





# Owners
class OwnerCreateAPIView(CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

owner_create_view = OwnerCreateAPIView.as_view()

class OwnerUpdateAPIView(UpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

owner_update_view = OwnerUpdateAPIView.as_view()

class OwnerDestroyAPIView(DestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

owner_destroy_view = OwnerDestroyAPIView.as_view()

class OwnersListAPIView(ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

owners_view = OwnersListAPIView.as_view()






