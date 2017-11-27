from django.db          import models
from photo.models       import Photo
from photoseries.models import Photoseries
from photoseries        import models
# Create your models here.
class Cart(models.Model):
    owner = models.ForeignKey(Profile)
    #Entweder many2many oder lsite mit bild ids
    images = models.ManyToManyField(Photo)
    #images = []
    #add methoden etc? spart eine Tabelle
    series = models.ManyToManyField(Photoseries) 
    sent = False
    payed = False