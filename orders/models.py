from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo
from photoseries.models import Photoseries

from dynamicLink.models import Download
from dynamicLink.presettings import DYNAMIC_LINK_URL_BASE_COMPONENT

# Create your models here.
def build_url(linkobject, langcode='lg'):
        """returns the access url of the of the dynamicLink object"""
        return '%s%s/%s/%s/link/%s/%s' % (
                                  'http://',
                                  # DIRTY HACK - CHANGE ME IN PROD!
                                  'localhost:8000',
                                  langcode,
                                  DYNAMIC_LINK_URL_BASE_COMPONENT,
                                  linkobject.link_key,
                                  linkobject.get_filename()
)

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
    # Download links for every photo inside this order
    downloads = models.ManyToManyField(Download)

    def getTotalPrice():
        # Calculates the total price of this order
        totalSum = 0
        for photo in this.photoseries:
            totalSum += photo.price
        for singel_photoseries in this.photoseries:
            totalSum += singel_photoseries.price
        return totalSum 

    def get_download_links(self):
        links = []
        for download in self.downloads.all():
            if not download.active:
                return None
            links.append(build_url(download, 'en'))
        return links