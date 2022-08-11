from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('language', views.LanguageView)
router.register('document', views.DocumentView)
router.register('page', views.PageView)

urlpatterns = router.urls