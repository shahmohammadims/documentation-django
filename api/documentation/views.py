from .models import Language, Document, Page
from .serializers import LanguageSerializer, DocumentSerializer, PageSerializer
from rest_framework import viewsets


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        documents = Document.objects.all()
        filter = self.request.GET.get('language')
        if filter is not None:
            return documents.filter(language=filter)
        return documents


class PageView(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    
    def get_queryset(self):
        pages = Page.objects.all()
        filter = self.request.GET.get('document')
        if filter is not None:
            return pages.filter(document=filter)
        return pages