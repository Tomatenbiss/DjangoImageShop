from django.db import models
from photograph.models import Photo
# Create your models here.

class Photoseries(models.Model):
    title       = models.CharField(max_length=20)
    describtion = models.CharField(max_length=100)
    images      = models.ManyToManyField(Photo)
    tags        = []
    #owner      = models.ForeignKey(User)

    
