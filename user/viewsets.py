from rest_framework import viewsets
from . models import Me
from .serializers import MeSerializer

class MeViewSet(viewsets.ModelViewSet):
    queryset = Me.objects.all()
    serializer_class = MeSerializer
    