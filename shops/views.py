from django.contrib.auth.models import User, Group
from django.views.generic import ListView, TemplateView

from photos.models import Photo
from photoseries.models import Photoseries

class viewAllPhotos(TemplateView):
    template_name = 'shops/shop_view.html'

    def get_context_data(self, **kwargs):
        ''' Only retrieve photos and photoseries which are visible and match the requested photographer '''
        username = self.kwargs['username']
        context = super(viewAllPhotos, self).get_context_data(**kwargs)
        context['shop_exists'] = True
        try:
            user = User.objects.get(username=username)
            if user.groups.filter(name='photographer').exists():
                context['photos'] = Photo.objects.filter(public=True, owner=user, order_copy=False)
                context['photoseries_list'] = Photoseries.objects.filter(public=True, owner=user, order_copy=False)
        except User.DoesNotExist:
            context['shop_exists'] = False
            return context
        return context


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
