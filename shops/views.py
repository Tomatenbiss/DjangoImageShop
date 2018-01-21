from django.contrib.auth.models import User, Group
from django.views.generic import ListView

from photos.models import Photo


class viewAllPhotos(ListView):
    model = Photo
    template_name = 'shops/photo_list.html'

    def get_queryset(self):
        ''' Only retrieve photos which are visible and match the requested photographer '''
        username = self.kwargs['username']

        try:
            user = User.objects.get(username=username)
            if user.groups.first().name == 'photographer':
                return Photo.objects.filter(public=True, owner=user, order_copy=False)
            else:
                return None
        except User.DoesNotExist:
            return None


class viewAllShops(ListView):
    model = Photo
    template_name = 'landingpage.html'

    def get_queryset(self):

        users = User.objects.all()
        photographer = []
        for user in users:

            if user.groups.first() is not None and user.groups.first().name == 'photographer':
                photographer.append(user)
        return photographer
