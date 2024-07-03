from django.db import models
from products.models import AbstractModel

# Create your models here.

class Blog(AbstractModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    slug = models.CharField(max_length=140)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title