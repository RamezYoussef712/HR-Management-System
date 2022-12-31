from django.urls import path, include
from rest_framework import routers
from .views import LeaveRequestViewSet

router = routers.DefaultRouter()
router.register(r'', LeaveRequestViewSet)

urlpatterns = router.urls

