from django.urls    import reverse
from django.db      import models
from django.contrib.auth.models     import User
#from accounts.models import Profile, Photographer
from django.core.exceptions     import ValidationError
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize, Adjust
from PIL import Image, ImageDraw, ImageFont
from .processors import TextOverlayProcessor

class Watermark(object):
    def process(self, img):
        watermark = "/root/djangogirls/tomatenbiss15/media/photos/200-star.png"
        scaled = ImageWatermark(watermark, position=('center', 'center'), scale=True, opacity=0.2)
        img_scaled = scaled.process(img)
        return img_scaled

class Photo(models.Model):
    #Bild aus Datei
    image       = models.ImageField(upload_to='photos', blank=True, null=True)
    #Beschreibung - max_l optional 
    description = models.TextField(max_length=200)
    #Besitzer 1:M
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #Kategorie M:N
    categories = models.ManyToManyField('PhotoCategory', blank=True)
    #modifiziert
    last_modified = models.DateTimeField(auto_now_add=True,editable=False)
    #uploadclass Photo(models.Model):

    created = models.DateTimeField(auto_now_add=True,editable=False)
    #Titel
    title = models.CharField(max_length=20)
    #sichtbar
    public = models.BooleanField(default=False)
    #Preis
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    #Zeigt an, ob das Bild nur für eine Bestellung erstellt wurde
    order_copy = models.BooleanField(default=False)

    shoppingcartview = ImageSpecField(source='image',
                                      processors=[ResizeToFill(80, 40)],
                                      format='PNG',
                                      options={'quality': 60})

    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(200, 100)],
                                      format='PNG',
                                      options={'quality': 60})

    watermarked_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(200, 100), TextOverlayProcessor(text='DjangoImageShop')],
                                      format='PNG',
                                      options={'quality': 60})

    detailview = ImageSpecField(source='image',
                                      processors=[ResizeToFill(730, 490)],
                                      format='PNG',
                                      options={'quality': 60})

    watermarked_detailview = ImageSpecField(source='image',
                                      processors=[ResizeToFill(730, 490), TextOverlayProcessor(text='DjangoImageShop')],
                                      format='PNG',
                                      options={'quality': 60})

    watermarked_image = ImageSpecField([Watermark(),ResizeToFill(730, 490)], source='image',
            format='PNG', options={'quality': 90})

    def __str__(self):
        return "%s : %s" % (self.title, self.owner)

    def clean(self):
        if self.price < 0.00:
            raise ValidationError({'price': 'The price can\'t be negative.'})
        # price has to be set as soon as the public attribute is true
        if self.public and self.price == 0.00:
            raise ValidationError({'price': 'The price has to be set, if you want to set the picture publicy visible.'})

    def get_absolute_url(self):
        return reverse('photos:view', kwargs={'pk': self.pk})


class PhotoCategory(models.Model):
    #Name der Kategorie
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.name)

    def clean(self):
        # this works because empty sequences are false
        if PhotoCategory.objects.filter(name=self.name):
            raise ValidationError({'name': 'This category already exists.'})

    def get_absolute_url(self):
        return reverse('photos:categories')

