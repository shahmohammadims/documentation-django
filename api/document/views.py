from .models import Language, Document, Page
from .serializers import LanguageSerializer, DocumentSerializer, PageSerializer
from rest_framework import viewsets


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class PageView(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer