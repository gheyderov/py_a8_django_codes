from django.contrib import admin
from products.models import Category, Tag, Recipe, ProductType, Property, PropertyValue

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(PropertyValue)
admin.site.register(Property)
admin.site.register(ProductType)
