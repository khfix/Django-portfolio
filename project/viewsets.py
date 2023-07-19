from rest_framework import viewsets
from rest_framework.response import Response
from .models import Project, Photo, programmingLang, Link, Hashtag, Code
from .serializers import ProjectSerializer, PhotoSerializer, ProgrammingLangSerializer, LinkSerializer, HashtagSerializer, CodeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        photos = Photo.objects.filter(project=instance)
        photo_serializer = PhotoSerializer(photos, many=True)

        prolangs = programmingLang.objects.filter(project=instance)
        prolangs_serializer = ProgrammingLangSerializer(prolangs, many=True)

        hashtags = Hashtag.objects.filter(project=instance)
        hashtags_serializer = HashtagSerializer(hashtags, many=True)

        links = Link.objects.filter(project=instance)
        links_serializer = LinkSerializer(links, many=True)

        codes = Code.objects.filter(project=instance)
        codes_serializer = CodeSerializer(codes, many=True)




        data = serializer.data
        data['photos'] = photo_serializer.data
        data['prolangs'] = prolangs_serializer.data
        data['hashtags'] = hashtags_serializer.data
        data['links'] = links_serializer.data
        data['codes'] = codes_serializer.data

        return Response(data)
    

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class ProgrammingLangViewSet(viewsets.ModelViewSet):
    queryset = programmingLang.objects.all()
    serializer_class = ProgrammingLangSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
