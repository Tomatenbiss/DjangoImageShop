from django.db          import models
from photos.models       import Photo
from django.contrib.auth.models     import User
from django.urls import reverse
# Create your models here.

class Photoseries(models.Model):
    title       = models.CharField(max_length=20)
    describtion = models.CharField(max_length=100)
    images      = models.ManyToManyField(Photo)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return (self.owner.username + " : " + self.title)

    def clean(self):
        if self.price < 0.00:
            raise ValidationError({'price': 'The price can\'t be negative.'})
        # price has to be set as soon as the public attribute is true
        if self.public and self.price == 0.00:
            raise ValidationError({'price': 'You have to set a price for the photoseries.'})

    def get_absolute_url(self):
        return reverse('view_series', kwargs={'pk': self.pk})
    
