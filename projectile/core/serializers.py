from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError

from .models import Person


class PersonBasicSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        ),
        read_only_fields = (
            'id',
        )


class PersonRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, allow_null=True, allow_blank=True, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate_password(self, value):
        confirm_password = self.initial_data.get('confirm_password')
        if confirm_password != value:
            raise ValidationError('Confirm password does not match!')
        return value

    def create(self, validated_data):
        # Remove the confirm password from the validated data
        del validated_data['confirm_password']
        return super(PersonRegistrationSerializer, self).create(validated_data)

    class Meta:
        model = Person
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'country',
            'gender',
            'hero_image',
            'password',
            'confirm_password'
        )


class PersonSerializer(ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'phone',
            'country',
            'language',
            'gender',
            'profile_image',
            'hero_image',
            'email_on_new_message',
            'email_on_new_like',
            'email_when_edit_link',
            'email_when_edit_list',
            'has_newsletter',
            'has_weekletter',
            'created_at',

        )
        read_only_fields = (
            'id',
            'created_at',
        )


class MeLoginSerializer(Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, obj, validated_data):
        pass
