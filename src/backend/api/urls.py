from django.urls import path
from .views import (
    product_detail_view,
    owner_create_view,
    product_create_view,
    product_list_view,
    product_list_create_view,
    owner_update_view,
    owners_view,
    owner_destroy_view,
    product_custom_api_view,
)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', product_custom_api_view, name='products'),
    path('<int:pk>/', product_custom_api_view, name='products-detail'),



    # Auth Token
    path('auth/', obtain_auth_token),
    

    # Products
    # path('all/', ProductMixinAPIView.as_view()),
    
    # path('all/<int:pk>/', ProductMixinAPIView.as_view()),








    

    # path('products/<int:pk>/', product_detail_view, name='product_detail'),

    # path('products/', product_create_view, name="create_product"),

    # path('<int:pk>/', product_list_create_view, name="products"),
    # path('c/', product_list_create_view, name="c"),




    # Owners
    path('owners/create/', owner_create_view, name='create_owner'),
    path('owners/all/', owners_view, name='owners'),
    path('owners/<int:pk>', owner_update_view, name='update_owner'),
    path('owners/d/<int:pk>', owner_destroy_view, name='delete_owner'),
]
