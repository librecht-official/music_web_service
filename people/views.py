from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer


class CreateUserView(generics.CreateAPIView):
    # CreateAPIView provide only POST Method
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        print('created: {} token: {}'.format(created, token))
        data = {'token': token.key, 'user': serializer.data}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


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