from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractModel):
    title = models.CharField('title', max_length=150)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title


class Tag(AbstractModel):
    title = models.CharField('title', max_length=150)
    
    def __str__(self) -> str:
        return self.title
    

class Recipe(AbstractModel):
    # product_type = models.ForeignKey('ProductType', related_name='recipes', null=True, blank=True, on_delete=models.CASCADE)
    # values = models.ManyToManyField('PropertyValue', related_name='recipes')

    title = models.CharField('title', max_length=255)
    cover_image = models.ImageField('cover_image', upload_to='products/')
    small_description = models.CharField('small_description', max_length=255)
    description = models.TextField('description')
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    

class RecipeImage(AbstractModel):
    image = models.ImageField(upload_to='recipe_images/')
    recipe = models.ForeignKey('Recipe', related_name='images', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.recipe.title
    

class ProductType(AbstractModel):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    

class Property(AbstractModel):
    product_type = models.ForeignKey(ProductType, related_name='properties', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    

class PropertyValue(AbstractModel):
    property_id = models.ForeignKey(Property, related_name='values', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title