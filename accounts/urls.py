from django.urls import path, re_path
from accounts.views import UserLoginView, register, logout, profile, activate

urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('register/', register, name = 'register'),
    path('profile/', profile, name = 'profile'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        activate, name='activate'),
]