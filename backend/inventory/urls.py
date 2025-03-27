from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, LeadViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'leads', LeadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
