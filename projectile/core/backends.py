from django.db.models import Q
from common.enums import Status
from .models import Person


class TEQAuthenticator(object):
    """Custom Omis User Authenticator class. This class
    logs in using any of pk, code, email and username of an active user

    Arguments:
        object
    
    Returns:
        Authenticator class
    """

    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        """this function is for getting a single user by pk
        
        Arguments:
            user_id {integer}
        
        Returns:
            User object
        """
        try:
            return Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return None

    def authenticate(self, username=None, password=None, email=None):
        """this function is basically used when anyone tries to login
        
        Arguments:
            username {string} -- username field
            password {string} -- the password of the user
        
        Returns:
            User object -- if success else returns None
        """
        # if phone field is passed treat it as username
        if email:
            username = email

        # if phone and username are not passed
        if not username or not password:
            return None

        try:
            # define how we want to query the database
            user = Person.objects.get(
                # parse the string to integer else error will be thrown for pk
                Q(username=username) |
                Q(email=username),
                status=Status.ACTIVE
            )
        except Person.DoesNotExist:
            return None

        return user if user.check_password(password) else None
