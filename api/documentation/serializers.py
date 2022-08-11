from rest_framework import serializers
from .models import Language, Document, Page


class LanguageSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Language
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'