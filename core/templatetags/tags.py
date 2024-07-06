from django import template

register = template.Library()
from products.models import Category, Recipe


@register.simple_tag
def get_categories(limit):
    categories = Category.objects.all()[:limit]
    return categories


@register.inclusion_tag("includes/recent_products.html")
def recent_recipes():
    recipes = Recipe.objects.all().order_by("-created_at")[:3]
    return {"recipes": recipes}
