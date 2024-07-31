# Generated by Django 5.0.6 on 2024-07-31 16:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ips',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.GenericIPAddressField(), blank=True, null=True, size=None),
        ),
    ]
