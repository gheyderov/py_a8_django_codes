from django.urls import path
from core.views import contact, home

urlpatterns = [
    path('contact/', contact, name = 'contact-us'),
    path('home/', home, name = 'homepage')
]