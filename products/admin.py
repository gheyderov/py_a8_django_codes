from django.contrib import admin
from products.models import (
    Category,
    Tag,
    Recipe,
    ProductType,
    Property,
    PropertyValue,
    RecipeImage,
    RecipeReview
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PropertyValue)
admin.site.register(Property)
admin.site.register(ProductType)
admin.site.register(RecipeImage)
admin.site.register(RecipeReview)


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


@admin.register(Recipe)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "get_tags", "author"]
    list_display_links = ["id", "title"]
    list_editable = ["category"]
    list_filter = ["category", "author__username"]
    list_per_page = 10
    search_fields = ["title", "category__title"]
    inlines = [RecipeImageInline]

    def get_tags(self, obj):
        tags = []
        for tag in obj.tags.all():
            tags.append(tag.title)
        return tags
