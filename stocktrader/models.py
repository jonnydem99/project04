from django.db import models
from .storage import OverwriteStorage

class Image(models.Model):
    image = models.ImageField(
        upload_to='uploaded/images', storage=OverwriteStorage())

