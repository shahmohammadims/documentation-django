from .models import Language, Document, Page
from .serializers import Languageserializer, Documentserializer, Pageserializer
from rest_framework import viewsets


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = Languageserializer


class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = Documentserializer


class PageView(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = Pageserializer