from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    def calculate_age(self):
        import datetime
        return int((datetime.date.today() - self.birth_date).days / 365.25  )
        age = property(calculate_age)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Photographer(Profile):
    profile = models.OneToOneField(Profile, parent_link=True, on_delete=models.CASCADE)
    # gibt noch keine shops
    # shop = OneToOneField(shop)
        
