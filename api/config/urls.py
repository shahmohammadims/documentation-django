from django.urls import path, include

urlpatterns = [
    path('user/', include('rest_framework.urls')),
    path('documentation/', include('documentation.urls')),
]
