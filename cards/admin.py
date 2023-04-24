from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CardModel,CategoryModel,CardImage
from django import forms

# Register your models here.
# admin.site.register(CardModel)
admin.site.register(CategoryModel)
admin.site.register(CardImage)

class MyModelForm(forms.ModelForm):
    class Meta:
        model = CardModel
        exclude = ['images']

class CardImageInline(admin.TabularInline):
    model = CardModel.images.through  # specifies the through model for the many-to-many relationship
    extra = 0  # sets the minimum number of extra forms to display

@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    inlines = [CardImageInline]
    form = MyModelForm

