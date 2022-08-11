from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', views.LanguageView)
router.register('document', views.DocumentView)
router.register('page', views.PageView)

urlpatterns = router.urls