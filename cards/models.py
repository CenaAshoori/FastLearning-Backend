
import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# from accounts.models import User
def get_file_path(instance, filename):
    wholename = filename.split('.')
    extension = wholename[-1]
    name = wholename[0]
    new_filename = f'{name}_{uuid.uuid4()}.{extension}'
    return 'uploads/files/' + new_filename
    
def get_image_path(instance, filename):
    wholename = filename.split('.')
    extension = wholename[-1]
    name = wholename[0]
    new_filename = f'{name}_{uuid.uuid4()}.{extension}'
    return 'uploads/images/' + new_filename

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.FileField(upload_to=get_image_path)
    

    def __str__(self):
        return self.title


class CardImage(models.Model):
    video_link = models.URLField(blank=True, null=True)
    isVideo = models.BooleanField(default=False)
    image = models.FileField(upload_to=get_image_path,blank=True, null=True)
    def clean(self):
        if not self.isVideo and (self.image is None or not self.image):
            raise ValidationError('Image is required if it is not a news')
    def __str__(self):
        return self.image.name or self.pk

class CardModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    images = models.ManyToManyField(CardImage)
    file = models.FileField(upload_to=get_file_path, blank=True, null=True)
    isPreview = models.BooleanField(default=True)

    NEWS = 'NW'
    FOLDER = 'FL'
    BOOK = 'BK'
    LESSON = 'LE'
    CATEGORY_CHOICES = [
        (NEWS, 'News'),
        # (FOLDER, 'Folders'),
        (BOOK, 'Books'),
        # (LESSON, 'Lessons'),
    ]
    category_type = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=BOOK,
    )
    # isNews = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.category_type != CardModel.NEWS and (self.file is None or not self.file):
            raise ValidationError('File is required if it is not a news')
        
    def save(self, *args, **kwargs):
        # update the timestamp whenever the object is saved
        self.updated_at = timezone.now()
        return super(CardModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
