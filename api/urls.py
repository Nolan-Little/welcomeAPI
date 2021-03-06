from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register('itineraries', views.ItineraryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
