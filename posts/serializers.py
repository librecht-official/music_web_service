from rest_framework import serializers
from .models import Post
from people.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_at', 'updated_at', 'user')