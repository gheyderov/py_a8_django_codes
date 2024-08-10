from products.models import Category, Tag, Recipe
from django.http import JsonResponse
from products.api.serializers import CategorySerializer, TagSerializer, RecipeSerializer
from rest_framework.decorators import api_view

def categories(request):
    category_lists = Category.objects.all()
    # category_dict = []
    # for category in category_lists:
    #     category_dict.append({
    #         'category_id': category.id,
    #         'title' : category.title
    #     })
    serializer = CategorySerializer(category_lists, many = True)
    return JsonResponse(serializer.data, safe = False)


def tags(request):
    tag_lists = Tag.objects.all()
    serializer = TagSerializer(tag_lists, many = True)
    return JsonResponse(serializer.data, safe = False)


@api_view(['GET', 'POST'])
def recipes(request):
    if request.method == 'POST':
        serializer = RecipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe = False)
        return JsonResponse(serializer.errors, safe = False)
    recipe_lists = Recipe.objects.all()
    serializer = RecipeSerializer(recipe_lists, many = True)
    return JsonResponse(serializer.data, safe = False)