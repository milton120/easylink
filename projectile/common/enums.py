from django.utils.translation import gettext as _

from enum import IntEnum, unique

def django_enum(cls):
    # decorator needed to enable enums in django templates
    cls.do_not_call_in_templates = True
    return cls

@unique
@django_enum
class Status(IntEnum):
    ACTIVE = 1
    DRAFT = 2
    INACTIVE = 3 
    REMOVED = 4
    DENIED = 5

@unique
@django_enum
class PublishStatus(IntEnum):
    GLOBAL = 1
    PRIVATE = 2
    WAS_PRIVATE_NOW_GLOBAL = 3
    WAS_GLOBAL_NOW_PRIVATE = 4
    SHARED_WITH_FRIENDS = 5
