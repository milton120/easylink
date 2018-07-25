import factory
import random

from common.enums import Status

from ..models import Person

# pylint: disable=no-init, old-style-class, too-few-public-methods
class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
    username = factory.Faker('first_name')
    email = factory.LazyAttribute(lambda person: '{}@example.com'.format(person.username))
    password = factory.PostGenerationMethodCall('set_password', 'testpass')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone = factory.Faker('phone_number')
    status = Status.ACTIVE
