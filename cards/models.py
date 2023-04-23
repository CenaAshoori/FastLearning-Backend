
import uuid
from django.db import models
# from accounts.models import User
def get_file_path(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{extension}'
    return 'uploads/files/' + new_filename
    
def get_image_path(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{extension}'
    return 'uploads/images/' + new_filename

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.FileField(upload_to=get_image_path)
    

    def __str__(self):
        return self.title

class CardModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.FileField(upload_to=get_image_path)
    file = models.FileField(upload_to=get_file_path)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title


