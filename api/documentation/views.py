from rest_framework import viewsets
from .models import Language, Documentation, Page
from .serializers import Languageserializer, Documentationserializer, Pageserializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = Languageserializer


class DocumentationViewSet(viewsets.ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = Documentationserializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = Pageserializer