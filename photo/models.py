from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    #Bild aus Datei
    image       = models.ImageField(upload_to='photos/', blank=True, null=True)
    #Beschreibung - max_l optional 
    description = models.TextField(max_length=200)
    #schonmal ne Liste fuer die Kategorien spaeter
    tags        = []
    #Besitzer 1:M
    owner = models.ForeignKey(User)
    #modifiziert
    last_modified = models.DateTimeField(auto_now_add=True,editable=False)
    #upload
    created = models.DateTimeField(auto_now_add=True,editable=False)
    #Titel
    title = models.CharField(max_length=20)
    #sichtbar
    public = False
    
    def __str__(self):
        return "%s : %s" % (self.title, self.owner)

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})
