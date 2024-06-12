from django.urls import path
from products.views import products

urlpatterns = [
    path('recipes/', products, name = 'recipes')
]