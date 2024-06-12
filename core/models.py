from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField('name', max_length=200)
    email = models.EmailField('email', max_length=200)
    subject = models.CharField('subject', max_length=200)
    message = models.TextField('message')