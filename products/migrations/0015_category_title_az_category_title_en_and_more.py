# Generated by Django 5.0.6 on 2024-08-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_blockedips'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='title'),
        ),
    ]
