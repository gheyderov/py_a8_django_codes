from django.urls import path
from core.views import contact, home

urlpatterns = [
    path('contact-us/', contact, name = 'contact'),
    path('', home, name = 'homepage')
]