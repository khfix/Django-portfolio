from rest_framework import serializers
from .models import Project, Photo, programmingLang, Link, Hashtag, Code



class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class ProgrammingLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmingLang
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    prolangs = ProgrammingLangSerializer(many=True, read_only=True)
    hashtags = HashtagSerializer(many=True, read_only=True)
    links = LinkSerializer(many=True, read_only=True)
    codes= CodeSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

