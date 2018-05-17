from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from .validators import unique_tag_name_by_owner
from .models import Tag

class TagSerializer(ModelSerializer):
    def validate_name(self, value):
        if unique_tag_name_by_owner(self, value, Tag):
            return value
        else:
            raise serializers.ValidationError(
                'YOU_HAVE_ALREADY_A_TAG_WITH_SAME_NAME')
    
    # pylint: disable=old-style-class, no-init
    class Meta:
        model = Tag
        fields = (
            'id',
            'alias',
            'name',
            'slug',
            'status',
        )
