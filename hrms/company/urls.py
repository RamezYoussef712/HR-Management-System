from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, DepartmentViewSet


router = routers.SimpleRouter()
router.register(r'company', CompanyViewSet)
router.register(r'department', DepartmentViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('/', include(router.urls))
# ]
