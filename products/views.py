from typing import Any
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Recipe, Category, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from products.forms import ReviewForm


# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 2

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['category_lists'] = Category.objects.all()
        return context


# def products(request):
#     recipes = Recipe.objects.all() # Select * from Recipe
#     categories = Category.objects.all()
#     context = {
#         'recipe_lists' : recipes,
#         'category_lists' : categories
#     }
#     return render(request, 'recipes.html', context)

class RecipeDetailView(FormMixin, DetailView):
    template_name = 'single.html'
    model = Recipe
    form_class = ReviewForm
    # success_url = reverse_lazy('product_detail')

    def get_success_url(self) -> str:
        return reverse_lazy('product_detail', kwargs = {'pk' : self.object.pk})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.recipe = self.object
        form.save()
        return super().form_valid(form)

# def product_detail(request, pk):
#     recipe = get_object_or_404(Recipe, id=pk)
#     categories = Category.objects.all()
#     context = {
#         'recipe' : recipe,
#         'categories' : categories
#     }
#     return render(request, 'single.html', context)