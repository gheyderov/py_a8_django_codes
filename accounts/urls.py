from django.urls import path
from accounts.views import login, register, logout, profile

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('register/', register, name = 'register'),
    path('profile/', profile, name = 'profile'),
]