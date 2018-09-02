from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


class CreateUserView(generics.CreateAPIView):
    # CreateAPIView provide only POST Method
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserProfileView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get']

    # def perform_update(self, serializer):
    #
    #     serializer.save()