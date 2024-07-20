from django.urls import path
from core.views import home, ContactView

urlpatterns = [
    path('contact-us/', ContactView.as_view(), name = 'contact'),
    path('', home, name = 'homepage')
]