from rest_framework import serializers
from .models import Language, Documentation, Page


class Languageserializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class Documentationserializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = '__all__'


class Pageserializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'