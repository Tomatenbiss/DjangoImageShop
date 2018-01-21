from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo
from photoseries.models import Photoseries

# Create your models here.
class Order(models.Model):
    # The one who placed the order
    buyer = models.ForeignKey(User, related_name="buyer_id")
    # The one who is going to be paid
    seller = models.ForeignKey(User, related_name="seller_id")
    # Photos of the order
    photos = models.ManyToManyField(Photo)
    # Photoseries of the order
    photoseries = models.ManyToManyField(Photoseries)
    # Indicating wether the seller marked this purchase as paid
    paid = models.BooleanField(default=False)
    # Date when the order was paid
    paidDate = models.DateTimeField(null=True,blank=True)

    def getTotalPrice():
        # Calculates the total price of this order
        totalSum = 0
        for photo in this.photoseries:
            totalSum += photo.price
        for singel_photoseries in this.photoseries:
            totalSum += singel_photoseries.price
        return totalSum 