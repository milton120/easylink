import logging
import pytz

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField

from common.models import (CreatedAtUpdatedAtBaseModel,
                           NameSlugDescriptionBaseModel,)
from common.enums import Status
from common.lists import COUNTRIES
from common.fields import TimestampImageField
from .managers import PersonManager
from .mixins import UserThumbFieldMixin
from .enums import PersonGender

logger = logging.getLogger(__name__)


class Person(AbstractBaseUser, PermissionsMixin, CreatedAtUpdatedAtBaseModel, UserThumbFieldMixin):
    """
    A custom User model

    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.

    A more descriptive tutorial can be found here
    http://www.caktusgroup.com/blog/2013/08/07/migrating-custom-user-model-django/
    """
    username = models.CharField(unique=True, max_length=30, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_('Designates whether the user '
                                               'can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Whether this user should be treated as active. '
                                                'Unselect this instead of deleting accounts.'))
    country = models.CharField(max_length=2, choices=COUNTRIES, db_index=True)
    language = models.CharField(max_length=2, default='en')
    phone = models.CharField(max_length=20, blank=True)
    gender = models.IntegerField(
        choices=[(choice.value, choice.name.replace("_", " ")) for choice in PersonGender],
        default=PersonGender.MALE.value)
    email_on_new_message = models.BooleanField(default=True)
    email_on_new_like = models.BooleanField(default=True)
    email_when_edit_link = models.BooleanField(default=True)
    email_when_edit_list = models.BooleanField(default=True)
    has_newsletter = models.BooleanField(default=True)
    has_weekletter = models.BooleanField(default=True)
    profile_image = TimestampImageField(
        upload_to='profiles/cover', blank=True, null=True)
    hero_image = TimestampImageField(
        upload_to='profiles/avatar', blank=True, null=True)


    objects = PersonManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = (,)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self):
        return u"{} {} - {}".format(self.first_name, self.last_name, self.email)

    def get_full_name(self):
        """ Returns the full name """
        name = u"{} {}".format(self.first_name, self.last_name)
        return name.strip()

    def get_short_name(self):
        return u"{}".format(self.email)

    def get_anonymous_user():
        person, _ = Person.objects.get_or_create(
            status=Status.INACTIVE.value,
            username='anonymous', email="anonymous@email.com")
        return person