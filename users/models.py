from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        _('email address'), 
        blank=False, 
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        })

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'