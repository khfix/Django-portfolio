from django.urls import include, path
from rest_framework import routers
from .viewsets import MeViewSet
from .serializers import MeSerializer



routers = routers.DefaultRouter()
routers.register('me', MeViewSet)



urlpatterns = [
    path('api/', include(routers.urls)),
]




