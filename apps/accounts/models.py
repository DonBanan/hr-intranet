from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from simple_history.models import HistoricalRecords

from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPES = (
        ('admin', _('Admin')),
        ('hrg', _('HR-generalist')),
        ('employee', _('Employee')),
        ('service', _('Service Account')),
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=60, choices=USER_TYPES, default='employee')
    gender = models.BooleanField(_('Gender'), null=True)
    is_ses = models.BooleanField(_('Simple Electronic Signature'), default=False)
    user_locked = models.BooleanField(default=False)
    seen_welcome = models.BooleanField(default=False)
    history = HistoricalRecords()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
