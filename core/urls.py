from django.urls import path
from core.views import home, ContactView, export

urlpatterns = [
    path('contact-us/', ContactView.as_view(), name = 'contact'),
    path('', home, name = 'home'),
    path('export/', export, name = 'export'),
]