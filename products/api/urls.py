from django.urls import path
from products.api.views import CategoryAPIView, tags, RecipeAPIView, RecipeUpdateView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name = 'categories'),
    path('tags/', tags, name = 'tags'),
    path('recipes/', RecipeAPIView.as_view(), name = 'recipes'),
    path('recipes/<int:pk>/', RecipeUpdateView.as_view(), name = 'recipe_update'),
]