import jwt
from django.conf import settings


def get_activation_token(profile):
    """
    Returns a sha256 hexdigest string"
    """
    profile_pk = profile.pk
    token = jwt.encode({'user_pk': profile_pk}, settings.SECRET_KEY, algorithm='HS256')
    return token


def extract_primary_key_from_token(token):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return data.get('user_pk')
    except jwt.exceptions.DecodeError:
        return None
