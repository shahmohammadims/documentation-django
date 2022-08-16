from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', views.LanguageView, basename='language')
router.register('document', views.DocumentView, basename='document')
router.register('page', views.PageView, basename='page')

urlpatterns = router.urls