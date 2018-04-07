from django.utils.translation import gettext as _

from enum import IntEnum, unique

def django_enum(cls):
    # decorator needed to enable enums in django templates
    cls.do_not_call_in_templates = True
    return cls

@unique
@django_enum
class PersonGender(IntEnum):
    MALE = 1
    FEMALE = 2
    TRANSSEXUAL = 3
    ANY = 4
