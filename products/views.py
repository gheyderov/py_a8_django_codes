from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Recipe, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from products.forms import ReviewForm, SubReviewForm, RecipeCreateForm


# Create your views here.

class RecipeCreateView(CreateView):
    template_name = 'create_story.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    template_name = 'create_story.html'
    form_class = RecipeCreateForm
    model = Recipe
    success_url = reverse_lazy('home')


class RecipeListView(ListView):
    model = Recipe # Recipe.objects.all()
    template_name = 'recipes.html'
    paginate_by = 2

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('searched')
        if category:
            queryset = queryset.filter(category__id = category)
        if tag:
            queryset = queryset.filter(tags__id = tag)
        if tag and category:
            queryset = queryset.filter(tags__id = tag, category__id = category)
        if search:
            queryset = queryset.filter(title__icontains = search)
        return queryset

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
    sub_form = SubReviewForm
    # success_url = reverse_lazy('product_detail')

    def get_success_url(self) -> str:
        return reverse_lazy('product_detail', kwargs = {'pk' : self.object.pk})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'parent' in self.request.POST:
            form = self.sub_form
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.parent_id = self.request.POST.get('parent', None)
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