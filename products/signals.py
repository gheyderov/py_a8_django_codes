from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Recipe
from django.utils.text import slugify

@receiver(post_save, sender=Recipe)
def slug(instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title) + str(instance.id)
        instance.save()