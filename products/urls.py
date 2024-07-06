from django.urls import path
from products.views import products, product_detail

urlpatterns = [
    path('recipes/', products, name = 'recipes'),
    path('recipe/<int:pk>/', product_detail, name = 'product_detail')
]