from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TiroViewSet

router = DefaultRouter()
router.register(r'tiros', TiroViewSet)

urlpatterns = router.urls

