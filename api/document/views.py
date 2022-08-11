from .models import Language, Document, Page
from .serializers import Languageserializer, Documentserializer, Pageserializer
from rest_framework.generics import ListCreateAPIView


class LanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = Languageserializer


class DocumentView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = Documentserializer


class PageView(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = Pageserializer