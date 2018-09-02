from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='posts')

urlpatterns = [
    path(r'', include(router.urls)),
]