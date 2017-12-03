from django.urls    import reverse
from django.db      import models
from django.contrib.auth.models     import User
#from accounts.models import Profile, Photographer
from django.core.exceptions     import ValidationError

class Photo(models.Model):
    #Bild aus Datei
    image       = models.ImageField(upload_to='photos/', blank=True, null=True)
    #Beschreibung - max_l optional 
    description = models.TextField(max_length=200)
    #schonmal ne Liste fuer die Kategorien spaeter
    tags        = []
    #Besitzer 1:M
    owner = models.ForeignKey(User)
    #Kategorie M:N
    #categories = models.ManyToManyField('PhotoCategory')
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

    def __str__(self):
        return "%s : %s" % (self.title, self.owner)

    def clean(self):
        if self.price < 0.00:
            raise ValidationError({'price': 'Der Preis darf nicht negativ sein.'})
        # price has to be set as soon as the public attribute is true
        if self.public and self.price == 0.00:
            raise ValidationError({'price': 'Der Preis muss gesetzt werden, wenn das Bild öffentlich sein soll.'})

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})

class PhotoCategory(models.Model):
    #Name der Kategorie
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.name)

    def clean(self):
        # this works because empty sequences are false
        if PhotoCategory.objects.filter(name=self.name):
            raise ValidationError({'name': 'Diese Kategorie existiert bereits.'})

    def get_absolute_url(self):
        return reverse('categories')
