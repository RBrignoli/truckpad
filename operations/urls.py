"""
API V1: operations Urls
"""
###
# Libraries
###
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from operations.views import DriverProfileViewSet, DriverReportViewSet, OriginDestinationViewSet

###
# Routers
###


""" Main router """
router = DefaultRouter()
router.register(r'driver', DriverProfileViewSet, basename='driver-profile')
router.register(r'report', DriverReportViewSet, basename='driver-report')
router.register(r'origin-destination', OriginDestinationViewSet, basename='origin-destination')

###
# URLs
###
urlpatterns = [
    path('', include(router.urls)),
]