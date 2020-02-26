from django.contrib.auth import authenticate, update_session_auth_hash
from rest_framework import serializers
from django.utils.translation import gettext as _
from .models import UserProfile


class HelloSerializer(serializers.Serializer):
    """Serializer for Hello API view"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for User Profile Object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """
        Creates a new user profile in the system
        """

        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        print(user.password)
        return user

    def update(self, instance, validated_date):
        """
        Handles the update and partial update function of the viewset, Hashes the password correctly if that's
        the case
        """
        for attr, value in validated_date.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance


class CustomAuthTokenSerializer(serializers.Serializer):
    user = serializers.CharField(label=_("Email"))

    def __init__(self, *args, **kwargs):
        super(CustomAuthTokenSerializer, self).__init__(*args, **kwargs)
        self.fields['password'] = serializers.CharField(
            label=_("Password"),
            style={'input_type': 'password'},
            trim_whitespace=False
        )

    def validate(self, attrs):
        username = attrs.get('user')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
