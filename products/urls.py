from django.urls import path
from products.views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
)

urlpatterns = [
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="product_detail"),
    path("recipe-create/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipe-create/<int:pk>/", RecipeUpdateView.as_view(), name="recipe_update"),
]
