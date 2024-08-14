# Generated by Django 5.0.6 on 2024-07-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_recipe_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedIps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(verbose_name='ip_address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]