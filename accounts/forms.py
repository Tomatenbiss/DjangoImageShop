from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date = forms.DateField(help_text='Required. Format: DD.MM.YYYY')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_photographer = forms.BooleanField(label='Im a photograper', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'first_name', 'last_name', 'password1', 'password2', )

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
