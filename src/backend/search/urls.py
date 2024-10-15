from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchListAPIView.as_view(), name='search-list'),
]
