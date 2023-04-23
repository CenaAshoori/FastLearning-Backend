from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CardModel,CategoryModel

# Register your models here.
admin.site.register(CardModel)
admin.site.register(CategoryModel)
