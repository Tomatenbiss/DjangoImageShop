from django.db          import models
from photo.models       import Photo
# Create your models here.

class Photoseries(models.Model):
    title       = models.CharField(max_length=20)
    describtion = models.CharField(max_length=100)
    images      = models.ManyToManyField(Photo)
    tags        = []
    owner      = models.ForeignKey('accounts.Photographer', verbose_name='Fotograf', on_delete=models.CASCADE)

    def __str__(self):
        return (self.owner.profile.name + " : " + self.title)

    
