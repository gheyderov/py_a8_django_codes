# Generated by Django 5.0.6 on 2024-07-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='bio'),
        ),
    ]
