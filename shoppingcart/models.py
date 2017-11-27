from django.db import models
from photo.models import Photo
from photoseries import models
# Create your models here.
class Cart(models.Model):
    owner = models.ForeignKey(Profile)
    images = models.ManyToManyField(Photo)
    #series = models.ManyToManyField
    sent = False
    payed = False