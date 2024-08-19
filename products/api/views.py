from products.models import Category, Tag, Recipe
from django.http import JsonResponse
from products.api.serializers import CategorySerializer, TagSerializer, RecipeSerializer, RecipeCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


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




# def tags(request):
#     tag_lists = Tag.objects.all()
#     serializer = TagSerializer(tag_lists, many = True)
#     return JsonResponse(serializer.data, safe = False)


class CategoryAPIView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class RecipeAPIView(ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreateSerializer
        return self.serializer_class


# @api_view(['GET', 'POST'])
# def recipes(request):
#     if request.method == 'POST':
#         serializer = RecipeCreateSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False, status = 201)
#         return JsonResponse(serializer.errors, safe = False, status = 400)
#     recipe_lists = Recipe.objects.all()
#     serializer = RecipeSerializer(recipe_lists, context = {'request':request}, many = True)
#     return JsonResponse(serializer.data, safe = False)


# @api_view(['PUT', 'PATCH'])
# def recipe_update(request, pk):
#     if request.method == 'PUT':
#         recipe = Recipe.objects.get(id=pk)
#         serializer = RecipeCreateSerializer(data = request.data, instance = recipe)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False, status = 201)
#         return JsonResponse(serializer.errors, safe = False, status = 400)
#     if request.method == 'PATCH':
#         recipe = Recipe.objects.get(id=pk)
#         serializer = RecipeCreateSerializer(data = request.data, partial = True, instance = recipe)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False, status = 201)
#         return JsonResponse(serializer.errors, safe = False, status = 400)
#     return JsonResponse(serializer.data, safe = False)

class RecipeUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()