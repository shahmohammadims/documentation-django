from django.urls import path
from . import views

urlpatterns = [
    path('language/', views.LanguageView.as_view())
]
