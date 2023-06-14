# Register your models here.
from django.contrib import admin
from .models import CardModel,CategoryModel,CardImage
from django import forms

from django.http import HttpResponseRedirect

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

from django.db import models

@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.CharField: {'widget': admin.widgets.AdminRadioSelect},
    # }
    widgets = {
            'category_type': admin.widgets.AdminRadioSelect,
        }
    inlines = [CardImageInline]
    form = MyModelForm

    def response_change(self, request, obj):
        # Define the URL to which you want to redirect
        if obj.isPreview:
            custom_url = '/cards/preview/'

            # Redirect to the custom URL using HttpResponseRedirect
            return HttpResponseRedirect(custom_url)
        return super().response_change(request,obj)


