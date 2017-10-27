from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Utilizator(User):
    gender_list = (
        ('M', 'Barbat'),
        ('F', 'Femeie')
    )
    data_nasterii = models.DateTimeField(null=True, )
    gender = models.CharField(choices=gender_list, max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
