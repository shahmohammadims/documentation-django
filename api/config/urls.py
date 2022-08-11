from django.urls import path, include

urlpatterns = [
    path('user/', include('rest_framework.urls')),
    path('document/', include('document.urls')),
]
