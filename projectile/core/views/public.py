import datetime
from django.contrib.auth import authenticate, login, logout

from rest_framework import serializers, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import MeLoginSerializer, PersonRegistrationSerializer
from core.models import Person
from core.permissions import IsAuthenticatedOrCreate
from common.enums import Status


class UserRegistration(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonRegistrationSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class MeLogin(APIView):

    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = MeLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(username=serializer.data['email'], password=serializer.data['password'])
            if user is not None:
                if user.is_active and user.status == Status.ACTIVE:
                    login(request, user)
                    return Response()
                else:
                    raise serializers.ValidationError('Please activate account.')
            else:
                raise serializers.ValidationError('Invalid login credentials. Try again.')


class MeLogout(APIView):

    def get(self, request, format=None):
        logout(request)
        return Response()
