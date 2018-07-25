from django.db.models import Prefetch
from rest_framework import generics, permissions
from common.enums import Status
from core.permissions import IsOwner
from core.models import Person

from .models import Tag, Category, Link
from .serializers import (
    TagSerializer,
    CategoryBasicSerializer,
    CategorySerializer,
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


class CategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        return CategoryBasicSerializer
    
    def get_queryset(self):
        return Category.objects.filter(
            status=Status.ACTIVE,
            entry_by=self.request.user
        )
    
    def perform_create(self, serializer, extra_fields=None):
        self.create_data = {}
        if hasattr(serializer.Meta.model, 'entry_by'):
            self.create_data['entry_by'] = self.request.user
            self.create_data['updated_by'] = self.request.user

        if extra_fields is not None:
            self.add_extra_fields(extra_fields)

        serializer.save(**self.create_data)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    serializer_class = CategoryBasicSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Category.objects.filter(
            status=Status.ACTIVE,
            entry_by=self.request.user
        )


class PublicLinkList(generics.ListCreateAPIView):
    """Get all links and create new one"""
    permission_classes = (
        permissions.AllowAny,
    )
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LinkSerializer
        return LinkBasicSerializer
    
    def get_queryset(self):
        tags = Tag.objects.filter(status=Status.ACTIVE.value,)
        return Link.objects.prefetch_related(
            Prefetch('tags', queryset=tags)
        ).select_related('category').filter(
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


class UserLinkList(generics.ListAPIView):
    """Get all Private links"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LinkSerializer

    def get_queryset(self):
        tags = Tag.objects.filter(status=Status.ACTIVE.value,)
        return Link.objects.prefetch_related(
            Prefetch('tags', queryset=tags)
        ).select_related('category').filter(
            status=Status.ACTIVE,
            entry_by=self.request.user
        ).order_by('-updated_at')
