from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data['username'])
        # custom auth model could be set in AUTH_USER_MODEL in settings.py
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'user_id', 'bio', 'location', 'birth_date')

    username = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)