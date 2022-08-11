from django.urls import path, include

urlpatterns = [
    path('documentation/', include('documentation.urls')),
]
