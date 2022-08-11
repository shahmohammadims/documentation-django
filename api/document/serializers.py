from rest_framework import serializers
from .models import Language, Document, Page


class Languageserializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class Documentserializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class Pageserializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'