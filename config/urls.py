from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/', include('rest_framework.urls')),
    path('documentation/', include('documentation.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
