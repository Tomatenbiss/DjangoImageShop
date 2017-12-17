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
                return Photo.objects.filter(public=True, owner=user)
            else:
                return None
        except User.DoesNotExist:
            return None
