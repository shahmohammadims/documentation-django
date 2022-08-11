from .models import Language, Documentation, Page
from .serializers import Languageserializer, Documentationserializer, Pageserializer
from rest_framework.generics import ListCreateAPIView


class LanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = Languageserializer


class DocumentationView(ListCreateAPIView):
    queryset = Documentation.objects.all()
    serializer_class = Documentationserializer


class PageView(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = Pageserializer