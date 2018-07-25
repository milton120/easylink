from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ImageField
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


class TagLiteSerializer(ModelSerializer):
    # pylint: disable=old-style-class, no-init
    class Meta:
        model = Tag
        fields = (
            'id',
            'slug',
            'name'
        )


class CategoryBasicSerializer(ModelSerializer):
    # pylint: disable=old-style-class, no-init
    class Meta:
        model = Category
        fields = (
            'id',
            'slug',
            'name',
            'status',
            'priority',
            'is_global',
            'image',
        )
        read_only_fields = (
            'id',
            'slug',
        )


class CategorySerializer(ModelSerializer):
    thumb_small = ImageField(source='get_thumb_small', read_only=True)
    # pylint: disable=old-style-class, no-init
    class Meta:
        model = Category
        fields = (
            'id',
            'slug',
            'name',
            'thumb_small',
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
    tags = TagLiteSerializer(many=True)
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
            'tags',
            'status',
            'is_global',
            'entry_by'
        )