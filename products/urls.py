from django.urls import path
from products.views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name = 'recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = 'product_detail')
]