from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics


class SearchListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = None
        results = Product.objects.none()
        q = self.request.GET.get('q')
        if q is not None:
            if request.user.is_authenticated:
                user = request.user
            results = qs.search(q, user)

        return results