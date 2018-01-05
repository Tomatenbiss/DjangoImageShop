from django.db          import models
from photos.models       import Photo
from django.contrib.auth.models     import User
from django.urls import reverse
# Create your models here.

class Photoseries(models.Model):
    title       = models.CharField(max_length=20)
    describtion = models.CharField(max_length=100)
    images      = models.ManyToManyField(Photo)
    tags        = []
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.owner.username + " : " + self.title)

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})
    
