"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from cards.views import CardListCreateView, CardRetrieveUpdateDestroyView,\
                        CategoryListCreateView, CategoryModelRetrieveUpdateDestroyView,download_file,download_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("accounts.urls")),
    path('cards/', CardListCreateView.as_view(), name='card-list-create'),
    path('cards/<int:pk>/', CardRetrieveUpdateDestroyView.as_view(), name='card-retrieve-update-destroy'),
    path('categories/', CategoryListCreateView.as_view(), name='Categories-list-create'),
    path('categories/<int:pk>/', CategoryModelRetrieveUpdateDestroyView.as_view(), name='Categories-retrieve-update-destroy'),
    path('uploads/files/<str:file_name>/', download_file, name='file'),
    path('uploads/images/<str:image_name>/', download_image, name='image'),

]

