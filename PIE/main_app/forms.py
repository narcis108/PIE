from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from main_app.models import Utilizator


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, required=True)

    class Meta:
        model = Utilizator
        fields = ('username', 'email', 'password1', 'password2',)
        labels = {
            'username': _('Utilizator'),
        }
        help_texts = {
            'username': _(''),
        }


