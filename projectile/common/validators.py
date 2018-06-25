from requests.models import PreparedRequest
from requests import exceptions
from django.core.exceptions import ValidationError

def url_validator(value):
    if value:
        prepared_request = PreparedRequest()
        try:
            prepared_request.prepare_url(value, None)
            return value
        except exceptions.MissingSchema:
            raise ValidationError("Invalid URL 'htt': No schema supplied. Perhaps you meant http://htt?")
