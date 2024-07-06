from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
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


def product_detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    categories = Category.objects.all()
    context = {
        'recipe' : recipe,
        'categories' : categories
    }
    return render(request, 'single.html', context)