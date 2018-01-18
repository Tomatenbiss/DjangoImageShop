from django.db          import models
from photos.models       import Photo
from django.contrib.auth.models     import User
# simple url reverse for Many2Many
from django.urls import reverse
# Create your models here.

class Photoseries(models.Model):
    # title of the series
    title       = models.CharField(max_length=20)
    # description of 100 characters
    description = models.CharField(max_length=100)
    # relation to images in the series
    images      = models.ManyToManyField(Photo)
    # owner gets set automatically on creation
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # price in float
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    # used to hide series from public
    public = models.BooleanField(default=False)

    # used for admin interface and database names
    def __str__(self):
        return (self.owner.username + " : " + self.title)

    # check for invalid price
    def clean(self):
        if self.price < 0.00:
            raise ValidationError({'price': 'The price can\'t be negative.'})
        # price has to be set as soon as the public attribute is true
        if self.public and self.price == 0.00:
            raise ValidationError({'price': 'You have to set a price for the photoseries.'})
    # needed for reverse
    def get_absolute_url(self):
        return reverse('view_series', kwargs={'pk': self.pk})
    
