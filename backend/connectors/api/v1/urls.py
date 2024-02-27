from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134056ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134056", Testconnectors134056ViewSet, basename="testconnectors134056"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
