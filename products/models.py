from django.db import models
from accounts.models import User

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
    title = models.CharField('title', max_length=255)
    cover_image = models.ImageField('cover_image', upload_to='products/')
    small_description = models.CharField('small_description', max_length=255)
    description = models.TextField('description')
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    # user = models.ForeignKey('User', related_name='recipes', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title