from django.urls import include, path
from rest_framework import routers
from .viewsets import ProjectViewSet, PhotoViewSet, ProgrammingLangViewSet, LinkViewSet, HashtagViewSet, CodeViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('photos', PhotoViewSet)
router.register('programming-langs', ProgrammingLangViewSet)
router.register('links', LinkViewSet)
router.register('hashtags', HashtagViewSet)
router.register('codes', CodeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
