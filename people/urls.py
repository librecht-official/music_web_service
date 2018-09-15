from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register(r'user_profile', views.UserProfileView, base_name='user_profile')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'register', views.CreateUserView.as_view(), name='register'),
    path(r'api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-token-auth', obtain_auth_token),
]
