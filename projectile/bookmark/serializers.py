from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from .validators import unique_tag_name_by_owner
from .models import Tag, Link, Category

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


class CategorySerializer(ModelSerializer):
    # pylint: disable=old-style-class, no-init
    category = Category
    class Meta:
        model = Link
        fields = (
            'id',
            'slug',
            'name',
        )


class LinkBasicSerializer(ModelSerializer):
    # pylint: disable=old-style-class, no-init
    class Meta:
        model = Link
        fields = (
            'id',
            'alias',
            'url',
            'name',
            'slug',
            'image',
            'description',
            'category',
            'status',
            'is_global'
        )
        read_only_fields = (
            'id',
            'slug',
        )


class LinkSerializer(ModelSerializer):
    # pylint: disable=old-style-class, no-init
    category = CategorySerializer()
    class Meta:
        model = Link
        fields = (
            'id',
            'alias',
            'url',
            'name',
            'slug',
            'image',
            'description',
            'category',
            'status',
            'is_global'
        )