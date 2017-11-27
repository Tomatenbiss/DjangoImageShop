from django.db import models
from django.contrib.auth.models import User
import os

class Photo(models.Model):
    #Titel
    title = models.CharField(max_length=20)
    #Bild aus Datei
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    #Beschreibung - Get new file name/upload pathmax_l optional 
    description = models.TextField(max_length=200)
    #schonmal ne Liste fuer die Kategorien spaeter
    tags        = []
    #Besitzer 1:M
    owner = models.ForeignKey(User)
    #modifiziert
    last_modified = models.DateTimeField(auto_now_add=True,editable=False)
    #upload
    created = models.DateTimeField(auto_now_add=True,editable=False)
    #sichtbar
    public = False
    def __str__(self):
        return "%s : %s" % (self.title, self.owner)

