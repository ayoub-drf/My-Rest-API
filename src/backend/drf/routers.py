from rest_framework.routers import DefaultRouter
from products.viewsets import ProductModelViewSet


router = DefaultRouter()
router.register('products', ProductModelViewSet, 'products')

urlpatterns = router.urls