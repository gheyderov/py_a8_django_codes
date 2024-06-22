from django.shortcuts import render
from products.models import Recipe, Category

# Create your views here.

def products(request):
    recipes = Recipe.objects.all() # Select * from Recipe
    categories = Category.objects.all()
    context = {
        'recipe_lists' : recipes,
        'category_lists' : categories
    }
    return render(request, 'recipes.html', context)


def product_detail(request):
    return render(request, 'single.html')