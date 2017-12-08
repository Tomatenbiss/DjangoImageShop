from django.db          import models
from photo.models       import Photo
from photoseries.models import Photoseries

from django.contrib.auth.models     import User

class Cart(models.Model):
    owner = models.ForeignKey(User)
    #Entweder many2many oder lsite mit bild ids
    images = models.ManyToManyField(Photo)
    #images = []
    #add methoden etc? spart eine Tabelle
    series = models.ManyToManyField(Photoseries) 
    sent = False
    payed = False
