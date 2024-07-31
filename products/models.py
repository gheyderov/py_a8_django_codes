from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()

# Create your models here.


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractModel):
    title = models.CharField("title", max_length=150)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Tag(AbstractModel):
    title = models.CharField("title", max_length=150)

    def __str__(self) -> str:
        return self.title


class Recipe(AbstractModel):
    # product_type = models.ForeignKey('ProductType', related_name='recipes', null=True, blank=True, on_delete=models.CASCADE)
    # values = models.ManyToManyField('PropertyValue', related_name='recipes')

    title = models.CharField("title", max_length=255)
    cover_image = models.ImageField("cover_image", upload_to="products/")
    small_description = models.CharField("small_description", max_length=255)
    description = models.TextField("description")
    category = models.ForeignKey(
        "Category", related_name="recipes", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField("Tag", related_name="recipes")
    author = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE)
    slug = models.SlugField('slug', null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs = {'slug' : self.slug})
    
    class Meta:
        ordering = ['-created_at']
        


class RecipeImage(AbstractModel):
    image = models.ImageField(upload_to="recipe_images/")
    recipe = models.ForeignKey(
        "Recipe", related_name="images", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.recipe.title


class RecipeReview(AbstractModel):
    parent = models.ForeignKey(
        "self", related_name="children", null=True, blank=True, on_delete=models.CASCADE
    )
    message = models.TextField()
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        "Recipe", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user.username} / {self.recipe.title}"


class ProductType(AbstractModel):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Property(AbstractModel):
    product_type = models.ForeignKey(
        ProductType, related_name="properties", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class PropertyValue(AbstractModel):
    property_id = models.ForeignKey(
        Property, related_name="values", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class BlockedIps(AbstractModel):
    ip_address = models.GenericIPAddressField('ip_address')