import time
from celery import shared_task
from core.models import Subscribe
from products.models import Recipe
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

@shared_task
def export_data():
    print('Process Start!')
    time.sleep(10)
    print('Process End!')



@shared_task
def send_email_to_subscribers():
    mail_lists = Subscribe.objects.values_list('email', flat=True)
    recipes = Recipe.objects.all()[:3]
    subject = 'New Products'
    message = render_to_string('email.html', {
        'recipes' : recipes
    })
    mail = EmailMultiAlternatives(
        subject = subject,
        body = message,
        from_email = settings.EMAIL_HOST_USER,
        to = mail_lists
    )
    mail.content_subtype = 'HTML'
    mail.send()
