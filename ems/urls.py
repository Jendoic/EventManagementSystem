from rest_framework.routers import DefaultRouter
from django.urls import path, include
from.views import *

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="cateories")
router.register(r"events", EventViewSet, basename="events")
router.register(r"rsvp", RSVPViewSet, basename="rsvp")


urlpatterns = [
    path("", include(router.urls)),
]