
from rest_framework import generics, permissions

from common.enums import Status
from core.permissions import IsOwner

from .models import Tag
from .serializers import TagSerializer


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
