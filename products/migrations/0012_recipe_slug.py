# Generated by Django 5.0.6 on 2024-07-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_recipereview_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
    ]