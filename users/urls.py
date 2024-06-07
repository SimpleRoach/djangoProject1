from django.urls import path
from . import views as users_views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', users_views.user_signup, name='sig'),
    path('login/', users_views.user_login, name='log')
]

