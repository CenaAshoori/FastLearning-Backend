from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register, logout

urlpatterns = [
    path("login/", view=obtain_auth_token),
    path("register/", view=register),
    path('logout/', view=logout),
]
