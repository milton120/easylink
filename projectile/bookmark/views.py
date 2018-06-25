
from rest_framework import generics, permissions
from common.enums import Status
from core.permissions import IsOwner
from core.models import Person

from .models import Tag, Link
from .serializers import (
    TagSerializer,
    LinkBasicSerializer,
    LinkSerializer,
)


class TagList(generics.ListCreateAPIView):
    """Get all tags and create new one"""

    permission_classes = (
        IsOwner,
    )
    serializer_class = TagSerializer
    
    def get_queryset(self):
        return Tag.objects.filter(
            status=Status.ACTIVE,
            entry_by=self.request.user
        ).order_by('name')
    
    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'entry_by'):
            self.create_data['entry_by'] = self.request.user
            self.create_data['updated_by'] = self.request.user

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)


class PublicLinkList(generics.ListCreateAPIView):
    """Get all links and create new one"""
    permission_classes = (
        permissions.AllowAny,
    )
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LinkSerializer
        else:
            return LinkBasicSerializer
    
    def get_queryset(self):
        return Link.objects.filter(
            status=Status.ACTIVE,
            entry_by=Person.get_anonymous_user()
        ).order_by('-updated_at')

    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'entry_by'):
            if self.request.user.id:
                self.create_data['entry_by'] = self.request.user
                self.create_data['updated_by'] = self.request.user
            else:
                self.create_data['entry_by'] = Person.get_anonymous_user()
                self.create_data['updated_by'] = Person.get_anonymous_user()

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)
